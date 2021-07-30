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