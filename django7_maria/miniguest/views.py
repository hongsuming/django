from django.shortcuts import render
from miniguest.models import Guest
from datetime import datetime
from django.http.response import HttpResponseRedirect

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def listFunc(request):
    list = Guest.objects.all() # 전체 레코드 읽기
    
    # print(Guest.objects.get(id=1))      # 1개 Guest object (1)
    # print(Guest.objects.filter(id=1))   # 여러 개 <QuerySet [<Guest: Guest object (1)>]>
    # print(Guest.objects.filter(title='성공'))   # 여러 개 <QuerySet [<Guest: Guest object (3)>]>
    # print(Guest.objects.filter(content__contains='버스')) # <QuerySet [<Guest: Guest object (2)>]>
    # print(Guest.objects.all().order_by('title')) # <QuerySet [<Guest: Guest object (3)>, <Guest: Guest object (1)>, <Guest: Guest object (2)>]>
    # print(Guest.objects.all().order_by('-title')) # 내림차순 <QuerySet [<Guest: Guest object (2)>, <Guest: Guest object (1)>, <Guest: Guest object (3)>]>
    # print(Guest.objects.all().order_by('-id')[0:2]) # <QuerySet [<Guest: Guest object (3)>, <Guest: Guest object (2)>]>
    # print(Guest.objects.all().order_by('title', '-id')) # <QuerySet [<Guest: Guest object (3)>, <Guest: Guest object (1)>, <Guest: Guest object (2)>]>
    
    return render(request, 'list.html', {'list':list})

def insertFunc(request):
    return render(request, 'insert.html')

def submitFunc(request):
    if request.method == 'POST':
        # insert
        Guest(
                title = request.POST.get('title'),
                content = request.POST.get('content'),
                regdate = datetime.now()
            ).save()
            
        # update
        # g = Guest.objects.get(id=수정할 id)
        # g.title = '수정할 값'
        # g.save()
        
        # delete
        # g = Guest.objects.get(id=삭제할 id)
        # g.delete()
    return HttpResponseRedirect('/guest/') # 단순히 list.html로 가면 안 됨

def deleteFunc(request):
    Guest.objects.get(id = request.GET.get("id")).delete()
    return HttpResponseRedirect('/guest/')