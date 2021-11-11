from django.shortcuts import render
from myapp.models import Buser, Jikwon
from django.http.response import HttpResponse
import json

# Create your views here.
def listFunc(request):
    blist = Buser.objects.all()
    return render(request, 'jikwonlist.html', {'blist' : blist})

def jiwonFunc(request):
    jlist = Jikwon.objects.filter(buser_num=request.GET["buser_no"])
    datas = []
    for j in jlist:
        dic = {'no' : j.jikwon_no, 'name' : j.jikwon_name, 'jik' : j.jikwon_jik}
        datas.append(dic);
    return HttpResponse(json.dumps(datas), content_type='application/json')