from django.shortcuts import render
from django.http import JsonResponse
from .models import Parameters
from .forms import FilterForm
import json
from decimal import Decimal


var_particle_map = {
    "D0": 'D0',
    "Dplus": 'D+',
    "Ds": 'Ds',
    "Ds0": 'D*0',
    "Dsplus": 'D*+',
    "Dss": 'Ds*',
    "Dsss": 'D**',
    "Dssss": 'Ds**',
}


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
                        dic_final[item]['unit'] = "$"+f'10^{str(unit)}'+"$"
                        dic_final[item]['value'] = "$" + \
                            str(latex_result_index(unit, digits, value, error))+"$"
                        result_json.append(dic_final[item])
                        dic_final[item]['id'] = str(dic[item]['id'])
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
        return f'< {value/unit:.{digits}f}'
    result = f'{(value/unit):.{digits}f}'
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
        print (pdg_val)
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
            dic['chi2'] = round(measurement['chi2'],2)
            if 'comments' in measurement.keys():
                dic['comments'] = measurement['comments']
            else:
                dic['comments']= None
            if 'latex' in measurement.keys():
                dic['measurement'] = "$"+measurement['latex']+"$"
            measurements_red_list.append(dic)
        else:
            dic = {}
            dic["experiment"] = measurement['experiment']
            dic['link'] = measurement['link']
            dic['text'] = measurement['text']
            dic['chi2'] = round(measurement['chi2'],2)
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

    return render(request, "detail.html", {'title': id, 'id': id, 'image_url': image_url, 'latex': par.data['latex'],
                                           'unit': unit, 'avg': avg, 'chi2_avg': chi2_avg, 'ndf_avg': ndf_avg, 'p': p, 'pdg_value': pdg_val, 'pdg_link': pdg_link,
                                           'measurement_list': measurements_list, 'measurement_red_list': measurements_red_list, })
