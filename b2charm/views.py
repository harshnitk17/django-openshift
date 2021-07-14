from django.shortcuts import render
from django.http import JsonResponse
from .models import Parameters
from .forms import FilterForm
import json

var_particle_map ={
    "D0":'D0' ,
    "Dplus":'D+',
    "Ds":'Ds',
    "Ds0":'D*0',
    "Dsplus":'D*+',
    "Dss":'Ds*',
    "Dsss":'D**', 
    "Dssss":'Ds**',
}
def build_config(data):
    config={}
    if data['initial']:
        config[str(data['initial'])] = 1
    if data['observable']:
        config[str(data['observable'])] = 1
    for particle in var_particle_map:
        if data[str(particle)]!= 0:
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
                    if config.items() <= dic[item]['filter'].items():
                        dic[item]['latex'] = "$"+str(dic[item]['latex'])+"$"
                        result_json.append(dic[item])                        

            del results
            del dic
            del config

            return JsonResponse(json.dumps(result_json), safe=False, content_type="application/json", status=200)
        else:
            return JsonResponse(json.dumps({"error": "some form error"}),
                                content_type="application/json", status=400)


