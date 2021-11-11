from django.shortcuts import render

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def page1Func(request):
    return render(request, 'page1.html')

def page2Func(request):
    return render(request, 'page2.html')

def page3Func(request):
    return render(request, 'page3.html')

def page4Func(request):
    return render(request, 'page4.html')

def page5Func(request):
    return render(request, 'page5.html')

def mycartFunc(request):
    name = request.POST["name"]
    price = request.POST["price"]
    # print(name, price)
    product = {'name' : name, 'price' : price}
    
    productList = [] # 장바구니에 물건 담기(상품명, 가격)를 각각을 담는 전체 기억 장소
    
    if "mycart" in request.session:
        productList = request.session["mycart"] # "mycart" session을 꺼내서
        productList.append(product)             # 장바구니에 물건을 담고
        request.session["mycart"] = productList # 다시 "mycart" 이름으로 session에 넣어줌
    else:
        productList.append(product)
        request.session["mycart"] = productList
        
    print('productList : ', productList)
    context = {}                                    # 데이터를 넘겨주려면 dict 타입이여야 돼서 context 생성
    context["products"] = request.session["mycart"] # productList를 담고 있는 "mycart" session을 넣어서 넘겨줌
    return render(request, 'mycart.html', context)

def buyFunc(request): # 결제 처리
    if "mycart" in request.session:
        productList = request.session["mycart"]
        # print(productList)
        total = 0
        for p in productList:
            total += int(p['price'])
        request.session.clear() # 세션 제거
    return render(request, 'buy.html', {'tot':total})
