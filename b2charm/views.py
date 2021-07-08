from django.shortcuts import render
from django.http import JsonResponse
from .models import Parameters
from .forms import FilterFormInitial
import json

def index(request):
    form = FilterFormInitial()
    return render(request, "index.html", {'form':form })

def post_form(request):
    if request.is_ajax and request.method == "POST":
        form = FilterFormInitial(request.POST)
        if form.is_valid():
            initial = form.cleaned_data.get('initial')
            results = Parameters.objects.all()
            dic={}
            result_json = []
            for obj in results:
                dic[str(obj.id)] = obj.data
            for item in dic:
                if 'filter' in dic[item].keys():
                    if str(initial) in dic[item]['filter']:
                        result_json.append(dic[item])
            del results
            del dic
            return JsonResponse(json.dumps(result_json), safe = False, content_type="application/json", status=200)
        else:
            return JsonResponse(json.dumps({"some error"}),
            content_type="application/json", status=400)


