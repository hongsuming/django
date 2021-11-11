from django.shortcuts import render
from mysangpum.models import Sangdata
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def listFunc(request):
    """
    페이징 처리가 없는 경우
    list = Sangdata.objects.all()
    return render(request, 'list2.html', {'list' : list})
    """
    # 페이징 처리가 있는 경우
    list = Sangdata.objects.all().order_by('-code')
    paginator = Paginator(list, 5) # 페이지 당 행 출력 수
    try:
        page = request.GET.get('page') # 페이지를 적어주면 ?page=
    except :
        page = 1 # 페이지를 안 적어주면 1페이지로
        
    try:
        data = paginator.page(page)
    except PageNotAnInteger: # 페이지가 정수가 아닌 경우
        data = paginator.page(1)
    except EmptyPage: # 페이지가 받아지지 않는 경우
        data = paginator.page(paginator.num_pages())
        
    # 개별 페이지 표시용 작업
    allpage = range(paginator.num_pages + 1)
    return render(request, 'list.html', {'sangpums' : data, 'allpage' : allpage})

def insertFunc(request):
    return render(request, 'insert.html')

def insertokFunc(request):
    if request.method == 'POST' :
        try:
            # 코드번호가 있는 경우
            Sangdata.objects.get(code=request.POST["code"])
            return render(request, 'insert.html', {'msg' : '이미 존재하는 코드입니다. 다른 번호를 입력하세요.'})
        except Exception as e:
            # 코드번호가 없는 경우
            Sangdata (
                code = request.POST["code"],
                sang = request.POST["sang"],
                su = request.POST["su"],
                dan = request.POST["dan"]
            ).save()
    return HttpResponseRedirect('/sangpum/list')

def updateFunc(request):
    data = Sangdata.objects.get(code=request.GET.get("code"))
    return render(request, 'update.html', {'data' : data})

def updateokFunc(request):
    if request.method == 'POST' :
        s = Sangdata.objects.get(code=request.POST["code"])
        s.sang = request.POST["sang"]
        s.su = request.POST["su"]
        s.dan = request.POST["dan"]
        s.save()
    return HttpResponseRedirect('/sangpum/list')

def deleteFunc(request):
    Sangdata.objects.get(code=request.GET["code"]).delete()
    return HttpResponseRedirect('/sangpum/list')