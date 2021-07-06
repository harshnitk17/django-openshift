from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Parameters
from .forms import FilterForm
import json

def index(request):
    form = FilterForm()
    return render(request, "index.html", {'form':form })

def post_form(request):
    if request.is_ajax and request.method == "POST":
        form = FilterForm(request.POST)
        if form.is_valid():
            initial = form.cleaned_data.get('initial')
            final = form.cleaned_data.get('final')
            print (initial,"/",final)
            config = {
                "initial":initial,
                "final":final
            }
            json_res = json.dumps(config)
            return JsonResponse(json_res, content_type="application/json",status=200)
        else:
            return JsonResponse(json.dumps({"some error"}),
            content_type="application/json", status=400)

