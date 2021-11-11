from django.shortcuts import render
from myapp.models import Article

# Create your views here.
def main(request):
    return render(request, 'main.html')

def dbtest(request):
    datas = Article.objects.all() # Django의 ORM (= select*from article)
    # print(datas)
    return render(request, 'articleList.html', {'articles' : datas})