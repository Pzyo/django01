from django.shortcuts import render,HttpResponse,redirect,reverse
from app01 import models

# Create your views here.

# def index(request):
#     """
#     :param request: 请求相关的所有数据对象
#     :return:
#     """
#     # return HttpResponse('你好呀')
#     return render(request, 'myfirst.html')  # 自动去templates目录寻找文件
#     # return redirect('https://www.mzitu.com/')

def login(request):
    # 返回一个登陆界面
    """
    get请求和post请求应该有不同的处理机制
    :param request: 请求相关的数据对象 里面有很多简易的方法
    :return:
    """
    # print(type(request.method))  # 返回请求方式 并且是全大写的字符串形式
    # if request.method == 'GET':
    #     return render(request,'login.html')
    # elif request.method == 'POST':
    #     return HttpResponse('收到了 宝贝')

    if request.method == 'POST':
        # 获取用户数据
        # print(request.POST) # 获取用户提交的post请求数据 (不包含文件)
        # <QueryDict: {'username': ['pzyo'], 'password': ['123']}>
        # username = request.POST.get('username')
        # print(username, type(username)) # pzyo <class 'str'>
        # hobby = request.POST.get('hobby')
        # print(hobby, type(hobby)) # 333 <class 'str'>

        """
        get只会获取列表最后一个元素
        """
        # username = request.POST.getlist('username')
        # print(username, type(username)) # ['admin'] <class 'list'>
        # hobby = request.POST.getlist('hobby')
        # print(hobby, type(hobby)) # ['111', '222'] <class 'list'>

        # 获取用户的用户名和密码 然后利用orm操作数据 校验数据是否正确
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 去数据库中查询数据
        from app01 import models
        # res = models.User.objects.filter(username=username)
        user_obj = models.User.objects.filter(username=username).first()
        # select * from user where username='pzyo';
        # user_obj = models.User.objects.filter(username=username,password=password).first()
        # select * from user where username='pzyo' and password='123';
        # <QuerySet [<User: User object>]> [数据对象1, 数据对象2, ...]
        # user_obj = res[0]
        # print(user_obj)
        # print(user_obj.username)
        # print(user_obj.password)
        if user_obj:
            # 比对密码是否一致
            if password == user_obj.password:
                return HttpResponse('登录成功')
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('用户不存在')
    # 获取url后面携带的参数 http://127.0.0.1:8000/login/?username=pzyo&password=123456
    # print(request.GET)  # 获取用户提交的get请求数据
    # <QueryDict: {'username': ['pzyo'], 'password': ['123'], 'hobby': ['111', '222', '333']}>
    # print(request.GET.get('hobby'))
    # print(request.GET.getlist('hobby'))
    """
    333
    ['111', '222', '333']
    """
    return render(request, 'login.html')

def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 直接获取用户数据存入数据库, 此处先不考虑校验用户是否已存在
        # 第一种增加
        # from app01 import models
        # res = models.User.objects.create(username=username,password=password)
        # # 返回值就是当前被创建的对象本身
        # print(res,res.username,res.password)

        # 第二种增加
        user_obj = models.User(username=username, password=password)
        user_obj.save()  # 保存数据

    # 先给用户返回一个注册页面
    return render(request,'reg.html')

def userlist(request):
    # 查询出用户表里面所有的数据
    # 方式1
    # data = models.User.objects.filter()
    # print(data)

    # 方式2
    user_queryset = models.User.objects.all()

    # return render(request, 'userlist.html',{'user_queryset':user_queryset})
    return render(request, 'userlist.html',locals())

def edit_user(request):
    # 获取url问号后面的参数
    edit_id = request.GET.get('user_id')
    # 查询当前用户想要编辑的数据对象
    edit_obj = models.User.objects.filter(id=edit_id).first()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 去数据库中修改对应的数据内容
        # 修改数据方式1
        # models.User.objects.filter(id=edit_id).update(username=username,password=password)
        """
            将filter查询出来的列表中所有的对象全部更新  批量更新操作
            只修改被修改的字段
        """

        # 修改数据方式2
        edit_obj.username = username
        edit_obj.password = password
        edit_obj.save()
        """
            上述方法当字段特别多的时候效率会非常的低
            从头到尾将数据的所有字段全部更新一遍, 无论该字段是否被修改
        """

        # 跳转到数据的展示页面
        return redirect('/userlist/')

    # 将数据对象展示到页面上
    return render(request, 'edit_user.html', locals())

def delete_user(request):
    # 获取用户想要删除的数据id值
    delete_id = request.GET.get('user_id')
    # 直接去数据库中找到对应的数据删除即可
    models.User.objects.filter(id=delete_id).delete()
    """
        批量删除
    """
    # 跳转到展示页面
    return redirect('/userlist/')

#def test(request):
def test(request,xx):
    print(xx)
    return HttpResponse('test')

#def testadd(request):
def testadd(request,year):
    print(year)
    return HttpResponse('testadd')

def home(request):
    # return HttpResponse('home')
    print(reverse('ooo'))
    # 无名分组反向解析
    print(reverse('xxx',args=(1,)))
    # 有名分组反向解析 写法1
    # print(reverse('sss',kwargs={'year':123}))
    # 简便的写法
    print(reverse('sss', args=(111,)))
    return render(request,'home.html')

def error(request):
    return HttpResponse('404 error')

# def index(request,args,year):
def index(request,*args,**kwargs):
    print(args)
    print(kwargs)
    return HttpResponse('index')

def func(request):
    return HttpResponse('func')

def index2(request):
    return HttpResponse('index2')

def func2(request,year):
    return HttpResponse('func2')