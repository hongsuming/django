from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
# 컨트롤러 역할 : 클라이언트의 요청을 urls.py가 받아서 컨트롤러로 전달해서 요청에 대한 처리

def index(request): # request 꼭 적어줘야 함
    msg = '장고 만세'
    ss = "<html><body>인덱스 요청 처리 %s</body></html>" %msg
    return HttpResponse(ss)

def helloFunc(request):
    name = '홍수민'
    age = '24'
    return render(request, 'show.html', {'name' : name, 'age' : age})

def worldFunc(request):
    return render(request, 'disp.html')