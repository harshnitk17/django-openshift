from django.shortcuts import render
from django.http import JsonResponse
from .models import Parameters, plot_info
from .forms import FilterForm
import json
from decimal import Decimal
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import date
from copy import deepcopy
import os
import uuid
import pathlib
from averaging.particles import var_particle_map,particle_filter_names,particle_categories


def build_config(data):
    config = {}
    if data['initial']:
        config[str(data['initial'])] = 1
    if data['observable']:
        config[str(data['observable'])] = 1
    for particle in var_particle_map:
        if data[str(particle)] != None and data[str(particle)] != 0:
            config[str(var_particle_map[particle])] = data[str(particle)]
    return config


def index(request):
    form = FilterForm()
    return render(request, "index.html", {'form': form})


def post_form(request):
    if request.is_ajax and request.method == "POST":
        form = FilterForm(request.POST)
        if form.is_valid():
            config = build_config(form.cleaned_data)
            results = Parameters.objects.all()
            dic = {}
            result_json = []
            for obj in results:
                dic[str(obj.id)] = obj.data
            for item in dic:
                if 'filter' in dic[item].keys():
                    if config and config.items() <= dic[item]['filter'].items():
                        dic[item]['latex'] = "$"+str(dic[item]['latex'])+"$"
                        dic_final = {}
                        dic_final[item] = {}
                        unit = int(dic[item]['unit_exp'])
                        digits = int(dic[item]['digits'])
                        value = float(dic[item]['value'])
                        error = []
                        if 'error_pos' in dic[item].keys():
                            error.append(float(dic[item]['error_pos']))
                            error.append(float(dic[item]['error_neg']))
                        else:
                            if 'error' in dic[item].keys():
                                error.append(float(dic[item]['error']))
                            else:
                                error = None
                        dic_final[item]['latex'] = "$" + \
                            str(dic[item]['latex'])+"$"
                        dic_final[item]['value'] = "$" + \
                            str(latex_result_index(unit, digits, value,
                                error))+" \\times "+"10^{"+str(unit)+"}$"
                        dic_final[item]['id'] = str(dic[item]['id'])
                        result_json.append(dic_final[item])
                        del dic_final, unit, digits, value, error

            del results
            del dic
            del config

            return JsonResponse(json.dumps(result_json), safe=False, content_type="application/json", status=200)
        else:
            return JsonResponse(json.dumps({"error": "some form error"}),
                                content_type="application/json", status=400)


def latex_error(unit, digits, error):
    """Return latex code for an uncertainty."""

    if len(error) == 1 or (round(error[0]/10**(unit), digits) == -round(error[1]/10**(unit), digits)):
        return f' \\pm{error[0]/10**(unit):.{digits}f}'
    else:
        return f'\,^{{+{error[0]/10**(unit):.{digits}f}}}_{{{error[1]/10**(unit):.{digits}f}}}'


def latex_result_index(unit, digits, value, error):
    """Return latex code for a measurement/average result in the given unit with "digits" digits after the dot."""

    digits = max(0, digits)
    if error is None:
        return f'< {value/10**(unit):.{digits}f}'
    result = f'{(value/10**(unit)):.{digits}f}'
    result += latex_error(unit, digits, error)
    return result


def latex_result(unit, digits, value, stat_error, syst_error=None):
    """Return latex code for a measurement/average result in the given unit with "digits" digits after the dot."""

    digits = max(0, digits)
    if stat_error is None:
        return f'< {value/10**(unit):.{digits}f}'
    result = f'{(value/10**(unit)):.{digits}f}'
    result += latex_error(unit, digits, stat_error)
    if syst_error is not None:
        result += latex_error(unit, digits, syst_error)
    return result


def view_detail(request, id):
    par = Parameters.objects.filter(data__id=id).first()
    image_url = str(id)+".png"
    unit = int(par.data['unit_exp'])
    digits = int(par.data['digits'])
    value = float(par.data['value'])
    error = []
    if 'error_pos' in par.data.keys():
        error.append(float(par.data['error_pos']))
        error.append(float(par.data['error_neg']))
    else:
        if 'error' in par.data.keys():
            error.append(float(par.data['error']))
        else:
            error = None
    if 'pdg_value' in par.data.keys():
        pdg_error = []
        if 'pdg_error_pos' in par.data.keys():
            pdg_error.append(float(par.data['pdg_error_pos']))
            pdg_error.append(float(par.data['pdg_error_neg']))
        else:
            if 'pdg_error' in par.data.keys():
                pdg_error.append(float(par.data['pdg_error']))
            else:
                pdg_error = None
        pdg_val = float(par.data['pdg_value'])
        pdg_val = "$" + str(latex_result_index(unit,
                            digits, pdg_val, pdg_error))+"$"
        pdg_link = par.data['pdg_link']
    else:
        pdg_val = None
        pdg_link = None
    avg = "$" + str(latex_result_index(unit, digits, value, error))+"$"
    chi2_avg = round(float(par.data['chi2']), 2)
    p = float(par.data['p'])
    p = '%.2E' % Decimal(p)
    if p[5] == '-':
        power = str(int(p[5:]))
    else:
        power = str(int(p[6:]))
    p = "$"+"p="+p[:4]+"\\times 10^{"+power+"}$"
    ndf_avg = int(par.data['ndf'])
    measurements = par.data['measurements']
    measurements_list = []
    measurements_red_list = []
    del digits
    for measurement in measurements:
        if 'color' in measurement.keys() and measurement['color'] == "red":
            dic = {}
            dic["experiment"] = measurement['experiment']
            dic['link'] = measurement['link']
            dic['text'] = measurement['text']
            if 'chi2' in measurement.keys():
                dic['chi2'] = round(measurement['chi2'], 2)
            if 'comments' in measurement.keys():
                dic['comments'] = measurement['comments']
            else:
                dic['comments'] = None
            if 'value' not in measurement.keys():
                if 'latex' in measurement.keys():
                    dic['measurement'] = "$"+measurement['latex']+"$"
            else:
                stat_error = []
                if 'stat_error_pos' in measurement.keys():
                    stat_error.append(float(measurement['stat_error_pos']))
                    stat_error.append(float(measurement['stat_error_neg']))
                else:
                    if 'stat_error' in measurement.keys():
                        stat_error.append(float(measurement['stat_error']))
                    else:
                        stat_error = None
                syst_error = []
                if 'syst_error_pos' in measurement.keys():
                    syst_error.append(float(measurement['syst_error_pos']))
                    syst_error.append(float(measurement['syst_error_neg']))
                else:
                    if 'syst_error' in measurement.keys():
                        syst_error.append(float(measurement['syst_error']))
                    else:
                        syst_error = None
                mes_val = float(measurement['value'])
                digits = int(measurement['digits'])
                dic['measurement'] = "$" + \
                    str(latex_result(unit, digits, mes_val,
                                     stat_error, syst_error))+"$"
            measurements_red_list.append(dic)
        else:
            dic = {}
            dic["experiment"] = measurement['experiment']
            dic['link'] = measurement['link']
            dic['text'] = measurement['text']
            if 'chi2' in measurement.keys():
                dic['chi2'] = round(measurement['chi2'], 2)
            if 'comments' in measurement.keys():
                dic['comments'] = measurement['comments']
            else:
                dic['comments'] = None
            if 'latex' in measurement.keys():
                dic['measurement'] = "$"+measurement['latex']+"$"
            else:
                stat_error = []
                if 'stat_error_pos' in measurement.keys():
                    stat_error.append(float(measurement['stat_error_pos']))
                    stat_error.append(float(measurement['stat_error_neg']))
                else:
                    if 'stat_error' in measurement.keys():
                        stat_error.append(float(measurement['stat_error']))
                    else:
                        stat_error = None
                syst_error = []
                if 'syst_error_pos' in measurement.keys():
                    syst_error.append(float(measurement['syst_error_pos']))
                    syst_error.append(float(measurement['syst_error_neg']))
                else:
                    if 'syst_error' in measurement.keys():
                        syst_error.append(float(measurement['syst_error']))
                    else:
                        syst_error = None
                mes_val = float(measurement['value'])
                digits = int(measurement['digits'])
                if 'using' in measurement.keys():
                    dic['measurement'] = "$" + str(latex_result(
                        unit, digits, mes_val, stat_error, syst_error))+"$"+" using "+measurement['using']
                else:
                    dic['measurement'] = "$" + \
                        str(latex_result(unit, digits, mes_val,
                            stat_error, syst_error))+"$"
            measurements_list.append(dic)
    del measurements
    correlations = par.data['correlations']
    correlations_list_fit = []
    correlations_list_external = []
    correlations_list_nuisance = []
    for correlation in correlations:
        dic = {}
        dic["type"] = str(correlation['type'])
        if "chi2" in correlation.keys():
            dic["chi2"] = round(correlation["chi2"], 2)
        else:
            dic["chi2"] = None
        if "correlation" in correlation.keys():
            dic["correlation"]=round(correlation["correlation"], 2)
        else:
            dic["correlation"]=None
        error = []
        if 'error_pos' in correlation.keys():
            error.append(float(correlation['error_pos']))
            error.append(float(correlation['error_neg']))
        else:
            if 'error' in correlation.keys():
                error.append(float(correlation['error']))
            else:
                error = None
        unit = int(correlation['unit_exp'])
        digits = int(correlation['digits'])
        value = float(correlation['value'])
        dic["value"] = "$" + str(latex_result_index(unit, digits,
                                 value, error)) + " \\times "+"10^{"+str(unit)+"}$"
        if dic["type"] == "fit":
            dic["latex"] = correlation['latex']
            dic["link"] = correlation["name"]
            correlations_list_fit.append(dic)
        elif dic['type'] == "external":
            dic["latex"] = correlation['latex']
            correlations_list_external.append(dic)
        elif dic['type'] == "nuisance":
            dic['latex'] = correlation["name"]
            correlations_list_nuisance.append(dic)
    del correlations
    unit = int(par.data['unit_exp'])
    return render(request, "detail.html", {'title': id, 'id': id, 'image_url': image_url, 'latex': par.data['latex'],
                                           'unit': unit, 'avg': avg, 'chi2_avg': chi2_avg, 'ndf_avg': ndf_avg, 'p': p, 'pdg_value': pdg_val, 'pdg_link': pdg_link,
                                           'measurement_list': measurements_list, 'measurement_red_list': measurements_red_list, 'correlation_list_fit': correlations_list_fit,
                                           'correlation_list_external': correlations_list_external, 'correlation_list_n': correlations_list_nuisance, })


def overview_plot(request):
    if request.is_ajax and request.method == "POST":
        selected = str(request.POST.get('selected')).rstrip(',').split(',')
        selected_dic = {}
        for bf in selected:
            data = Parameters.objects.filter(data__id=str(bf)).first().data
            selected_dic[str(bf)] = data
        file_id = uuid.uuid1()
        filename = str(pathlib.Path().resolve(
        ))+"/b2charm/static/b2charm/user_gen_plots/"+str(file_id)+".png"
        img_obj = plot_info(img_id=file_id, img_path=filename)
        img_obj.save()
        img_obj.chk_expiry()
        file_path = "/static/b2charm/user_gen_plots/"+str(file_id)+".png"
        _overview_plot(selected_dic, filename)
        return JsonResponse(json.dumps({"filepath": file_path}), safe=False, content_type="application/json", status=200)


dpi = 120


def hflav_logo(fig, scale=1):
    """Add the HFLAV logo to the figure"""
    subtitle = str(date.today())
    ypixel = 25
    xyratio = 4.8
    ysub = 0.9
    fontsize = 12
    fontsub = 0.75
    offset = -0.05
    xsize, ysize = fig.transFigure.inverted().transform(
        (scale * xyratio * ypixel, scale * (1 + ysub) * ypixel))
    fraction = ysub / (1 + ysub)
    font = {'family': 'sans-serif', 'style': 'italic',
            'color': 'white', 'weight': 'bold', 'size': scale * fontsize}

    save_axes = plt.gca()
    ax = plt.axes((0, 1-ysize, xsize, ysize), label='logo', frame_on=False)
    ax.set_axis_off()
    plt.fill([0, 1, 1, 0], [fraction, fraction, 1, 1],
             'k', edgecolor='k', linewidth=0.5)
    plt.text(0.5, 0.5 * (1 + fraction) + offset, 'HFLAV',
             fontdict=font, ha='center', va='center')
    plt.fill([0, 1, 1, 0], [0, 0, fraction, fraction],
             'w', edgecolor='k', linewidth=0.5)
    font['color'] = 'black'
    font['size'] *= fontsub
    plt.text(0.5, 0.5 * fraction + offset, subtitle,
             fontdict=font, ha='center', va='center')
    plt.sca(save_axes)


def _overview_plot(parameters, filename, title="Overview Plot for selected fractions"):
    """Create an overview plot."""

    # create the plot axes
    n = len(parameters)
    width = 10
    height = (n+3) * 0.4
    fig = plt.figure(figsize=(width, height), dpi=dpi, constrained_layout=True)
    ax = plt.axes()
    if title is not None:
        plt.title(title)
    plt.axis(ymin=0, ymax=n)
    plt.grid(True)

    # plot each parameter
    y = 0.5
    yticks = []
    xmin_zero = False
    for parameter in parameters:
        avg = parameters[parameter]['value']
        error = []
        if 'error_pos' in parameters[parameter].keys():
            error.append(float(parameters[parameter]['error_pos']))
            error.append(float(parameters[parameter]['error_neg']))
        else:
            if 'error' in parameters[parameter].keys():
                error.append(float(parameters[parameter]['error']))
                error.append(float(parameters[parameter]['error']))
            else:
                error = None
        plot, xmin_zero = plot_measurement(y, avg, error, None, xmin_zero)
        yticks.append(r'$' + parameters[parameter]['latex'] + '$')
        y += 1

    plt.yticks(0.5+np.arange(n), yticks)
    if xmin_zero:
        plt.xlim(left=0)

    # add logo and save figure
    hflav_logo(fig)
    plt.savefig(filename, format='png', dpi=dpi)
    plt.close()


def plot_measurement(y, value, stat_error, syst_error, xmin_zero, color='black', linestyle='solid'):
    """Add a measurement entry to a plot."""

    if value is None:
        return
    if stat_error is None:
        plot = plt.errorbar([value], [y], xerr=[[value], [
                            0]], xuplims=True, capsize=6, mew=2, color=color, linestyle=linestyle)
        plot[1][0].set_marker(matplotlib.markers.CARETLEFT)
        plot[1][0].set_markeredgewidth(0)
        if xmin_zero is False:
            xmin_zero = True
    else:
        error = deepcopy(stat_error)
        if syst_error is not None:
            error.append(syst_error)
        plot = plt.errorbar([value], [y], xerr=[[abs(error[1])], [
                            error[0]]], fmt='o', capsize=0, color=color, linestyle=linestyle)
        plt.errorbar([value], [y], xerr=[[abs(stat_error[1])], [
                     stat_error[0]]], capsize=6, mew=2, color=color)
        if value + error[1] < 0:
            xmin_zero = None

    return (plot, xmin_zero)
