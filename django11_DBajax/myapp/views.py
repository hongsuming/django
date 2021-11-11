from django.shortcuts import render
from myapp.models import Sangdata
from django.http.response import HttpResponse
import json

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def listFunc(request):
    return render(request, 'list.html')

def listDBFunc(request):
    sdata = Sangdata.objects.all()
    datas = []
    for s in sdata:
        dic = {'code' : s.code, 'sang' : s.sang, 'su' : s.su, 'dan' : s.dan}
        datas.append(dic)
        
    return HttpResponse(json.dumps(datas), content_type='application/json')