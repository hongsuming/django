from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
def MainFunc(request):
    return render(request, 'index.html')

class CallView(TemplateView):
    template_name = 'callget.html'
    
def insertFunc(request):
    if request.method == 'GET':
        return render(request, 'insert.html')
    elif request.method == 'POST':
        msg = request.POST.get("msg")
        # msg = request.POST["msg"] 위와 동일
        return render(request, 'list.html', {'message' : msg})
    else:
        print('요청 에러')
        
