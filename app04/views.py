from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import json
# Create your views here.

def ab_ajax(request):
    if request.method == 'POST':
        # print(request.POST) # <QueryDict: {'username': ['pzyo'], 'password': ['123']}>
        i1 = request.POST.get('i1')
        i2 = request.POST.get('i2')
        # 先转成整型再加
        i3 = int(i1) + int(i2)
        print(i3)
        d = {'code':100,'msg':i3}
        # return HttpResponse(i3)
        # return HttpResponse(json.dumps(d))
        return JsonResponse(d)

    return render(request, 'app04/index.html')

def index(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)

    return render(request,'app04/index2.html')

def ab_json(request):
    if request.is_ajax():
        # print(request.is_ajax())
        # print(request.POST)
        # print(request.FILES)
        # print(request.body)  # b'{"username":"pzoy","age":23}'

        # 针对json格式数据需要自己手动处理
        json_bytes = request.body
        # json_str = json_bytes.decode('utf-8')
        # json_dict = json.loads(json_str)

        # json.loads括号内部如果传了一个二进制格式的数据, 那么内部自动解码再反序列化
        json_dict = json.loads(json_bytes)
        print(json_dict,type(json_dict))

    return render(request,'app04/ab_json.html')

def ab_file(request):
    if request.is_ajax():
        if request.method == 'POST':
            print(request.POST)
            print(request.FILES)
    return render(request,'app04/ab_file.html')