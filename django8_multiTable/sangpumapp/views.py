from django.shortcuts import render
from sangpumapp.models import Maker, Product

# Create your views here.
def main(request):
    return render(request, 'main.html')

def list1(request):
    makers = Maker.objects.all()
    return render(request, 'list1.html', {'m' : makers})

def list2(request):
    products = Product.objects.all()
    pcount = len(products)
    return render(request, 'list2.html', {'p' : products, 'pc' : pcount})

def list3(request):
    maker = request.GET["id"]
    products = Product.objects.filter(maker_name=maker)
    pcount = len(products)
    return render(request, 'list2.html', {'p' : products, 'pc' : pcount})