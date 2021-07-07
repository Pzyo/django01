from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import json
from app04 import models
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

from django.core import serializers
def ab_ser(request):
    user_queryset = models.User.objects.all()
    # [{},{},{},{}]
    # user_list = []
    # for user_obj in user_queryset:
    #     tmp = {
    #         'pk':user_obj.pk,
    #         'username':user_obj.username,
    #         'age':user_obj.age,
    #         'gender':user_obj.get_gender_display()
    #     }
    #     user_list.append(tmp)
    # return render(request,'app04/ab_ser.html',locals())
    # return JsonResponse(user_list, safe=False)

    # 序列化
    res = serializers.serialize('json',user_queryset)
    """会自动帮你将数据变成json格式的字符串 并且内部非常的全面"""
    return HttpResponse(res)
"""
[
  {"age":23,"gender":"男","pk":1,"username":"pzyo"},
  {"age":18,"gender":"女","pk":2,"username":"xinxi"},
  {"age":50,"gender":"其他","pk":3,"username":"tank"},
  {"age":84,"gender":4,"pk":4,"username":"tony"}
]

前后端分离的项目
    作为后端开发, 只需要写代码将数据处理好
    能够序列化返回给前端即可
        再写一个接口文档 告诉前端每个字段代表的意思即可
       
#  serializers序列化组件
[
{   "model": "app04.user", 
    "pk": 1, 
    "fields": {"username": "pzyo", "age": 23, "gender": 1}}, 
{   "model": "app04.user", 
    "pk": 2, 
    "fields": {"username": "xinxi", "age": 18, "gender": 2}}, 
{   "model": "app04.user", 
    "pk": 3, 
    "fields": {"username": "tank", "age": 50, "gender": 3}}, 
{   "model": "app04.user", 
    "pk": 4, 
    "fields": {"username": "tony", "age": 84, "gender": 4}}
]
写接口利用序列化组件渲染数据然后写一个接口文档 该交代的交代下, 如gender对应关系
"""

def user_list(request):
    user_queryset = models.User.objects.all()
    return render(request,'app04/user_list.html',locals())

def delete_user(request):
    """
    前后端在用ajax进行交互的时候 后端通常给ajax的回调函数返回一个字典格式的数据
    :param request:
    :return:
    """
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {'code':1000,'msg':''}
            delete_id = request.POST.get('delete_id')
            models.User.objects.filter(pk=delete_id).delete()
            # 告诉前端操作结果
            back_dic['msg'] = '数据已删除'
            return JsonResponse(back_dic)