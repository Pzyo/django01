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

from utils.mypage import Pagination
def ab_pl(request):
    # 先给book插入1000条数据
    # for i in range(1000):
    #     models.Book.objects.create(title="第%s本书"%i)
    # 再将所有的数据查询并展示到前端页面
    # book_queryset = models.Book.objects.all()

    # 批量插入
    # book_list = []
    # for i in range(10000):
    #     book_obj = models.Book(title="第%s本书"%i)
    #     book_list.append(book_obj)
    # models.Book.objects.bulk_create(book_list)
    """
    当你想要批量插入数据的时候  使用orm给你提供的bulk_create能够大大的减少操作时间
    :param request:
    :return:
    """

    # 分页
    # book_list = models.Book.objects.all()

    # 想访问哪一页
    # current_page = request.GET.get('page', 1)  # 如果获取不到当前页码, 就展示第一页
    # 数据类型转换
    # try:
    #     current_page = int(current_page)
    # except Exception:
    #     current_page = 1
    # 每页展示多少条
    # per_page_num = 10
    # 起始位置
    # start_page = (current_page - 1) * per_page_num
    # 终止位置
    # end_page = current_page * per_page_num

    # 计算出到底需要多少页
    # all_count = book_list.count()
    # page_count, more = divmod(all_count, per_page_num)
    # if more:
    #     page_count += 1
    #
    # page_html = ''
    # xxx = current_page
    # if current_page < 6:
    #     current_page = 6
    # for i in range(current_page - 5, current_page + 6):
    #     if xxx == i:
    #         page_html += '<li class="active"><a href="?page=%s">%s</a></li>'%(i, i)
    #     else:
    #         page_html += '<li><a href="?page=%s">%s</a></li>' % (i, i)
    #
    # book_queryset = book_list[start_page:end_page]

    book_queryset = models.Book.objects.all()
    current_page = request.GET.get('page', 1)
    all_count = book_queryset.count()
    # 1. 传值生成对象
    page_obj = Pagination(current_page=current_page,all_count=all_count)
    # 2. 直接对总数据进行切片操作
    page_queryset = book_queryset[page_obj.start:page_obj.end]
    # 3. 将page_queryset传递到页面 替换之前的book_queryset

    return render(request,'app04/ab_pl.html',locals())

"""
per_page_num = 10

current_page        start_page          end_page
    1                   0                   10
    2                   10                  20
    3                   20                  30
    4                   30                  40
    
per_page_num = 5

current_page        start_page          end_page
    1                   0                   5
    2                   5                   10
    3                   10                  15
    4                   15                  20  
    
start_page = (current_page - 1) * per_page_num
end_page = current_page * per_page_num
"""