from django.shortcuts import render
from myfriend.models import Friend

# Create your views here.
def main(request):
    return render(request, 'main.html')

def friendList(request):
    datas = Friend.objects.all()
    return render(request, 'friendList.html', {'list' : datas})