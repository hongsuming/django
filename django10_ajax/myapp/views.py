from django.shortcuts import render
from django.http.response import HttpResponse

# 연습용 dict data
lan = {
    'id' : 111, 
    'name' : 'python',
    'history' : [
        {'date' : '2021-5-1', 'exam' : 'basic'},
        {'date' : '2021-6-1', 'exam' : 'django'},
    ]
}

import json
def testFunc():
    print(type(lan)) # <class 'dict'>
    
    # JSON 인코딩 : dict -> str로 변경
    jsonString = json.dumps(lan) 
    print(jsonString, type(jsonString)) # <class 'str'>
    
    # JSON 디코딩 : str -> dict로 변경
    dic = json.loads(jsonString)
    print(dic, type(dic)) # <class 'dict'>
    print(dic['name'])

# Create your views here.
def indexFunc(request):
    # 참고 : 파이썬 인코딩 / 디코딩
    testFunc()
    return render(request, 'index.html')

import time
def func1(request):
    msg = request.GET.get("msg")
    msg = 'nice' + msg
    
    time.sleep(5) # 지연시간 일부러 줘서 동기 방식 확인
    
    context = {'msg' : msg} # dict type 웹을 통해서 전송할 때는 str으로 바꿔 이진 처리 후 전송
    return HttpResponse(json.dumps(context), content_type='application/json')

def func2(request):
    datas = [
        {'name':'홍수민', 'age':24},
        {'name':'김진석', 'age':23},
        {'name':'홍재훈', 'age':22}
    ]
    return HttpResponse(json.dumps(datas), content_type='application/json') 

def func3(request):
    datas = [
        {'name':'홍수민', 'age':24},
        {'name':'김진석', 'age':23},
        {'name':'홍재훈', 'age':22}
    ]
    return HttpResponse(json.dumps(datas), content_type='application/json')