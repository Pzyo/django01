from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    print('我是视图函数index')
    obj = HttpResponse('index')

    def render():
        print('内部的render')
        return HttpResponse('O98K')

    obj.render = render
    return obj

def transfer(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        target_user = request.POST.get('target_user')
        money = request.POST.get('money')
        print('%s给%s转了%s元'%(username, target_user, money))
    return render(request, 'app07/transfer.html')

def transfers(request):
    return render(request, 'app07/transfers.html')