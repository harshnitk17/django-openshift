from django.shortcuts import render
from django.http import JsonResponse
from .models import Parameters
from .forms import FilterForm
import json


def index(request):
    form = FilterForm()
    return render(request, "index.html", {'form': form})


def post_form(request):
    if request.is_ajax and request.method == "POST":
        form = FilterForm(request.POST)
        if form.is_valid():
            try:
                initial = form.cleaned_data.get('initial')
            except:
                initial = None
            try:
                observable = form.cleaned_data.get('observable')
            except:
                observable = None
            results = Parameters.objects.all()
            dic = {}
            result_json = []
            for obj in results:
                dic[str(obj.id)] = obj.data
            for item in dic:
                if 'filter' in dic[item].keys():
                    if initial and observable and str(initial) in dic[item]['filter'] and str(observable) in dic[item]['filter']:
                        result_json.append(dic[item])
                    elif initial and not observable and str(initial) in dic[item]['filter']:
                        result_json.append(dic[item])
                    elif not initial and observable and str(observable) in dic[item]['filter']:
                        result_json.append(dic[item])

            del results
            del dic
            return JsonResponse(json.dumps(result_json), safe=False, content_type="application/json", status=200)
        else:
            return JsonResponse(json.dumps({"some error"}),
                                content_type="application/json", status=400)
