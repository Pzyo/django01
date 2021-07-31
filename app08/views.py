from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
# Create your views here.

"""
使用auth模块要用就用全套
"""

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 去用户表校验数据
        # 1. 表如何获取
        # 2. 密码如何比对
        user_obj = auth.authenticate(request, username=username, password=password)
        print(user_obj)  # 用户对象 数据不符合则返回None
        # print(user_obj.username)  # pzyo
        # print(user_obj.password)  # pbkdf2_sha256$260000$6jMFBDSSi6RiTYq8Zewz7S$YzAEX81MhXgIsP3/w2uxbNdwibCUbK5AQUZKt+FoznA=
        # 判断当前用户是否存在
        if user_obj:
            # 保存用户状态
            auth.login(request, user_obj)  # 类似于 request.session[key] = user_obj
            # 只要执行了该方法, 就可以在任何地方通过request.user获取到当前登录的用户对象
            return redirect('/app08/home/')
        """
        1. 自动查找auth_user表
        2. 自动给密码加密再比对
        该方法的注意事项
            括号内必须同时传入用户名和密码
            不能只传用户名(一步就帮你筛选出用户对象)
        """
    return render(request, 'app08/login.html')

from django.contrib.auth.decorators import login_required

"""
1. 如果局部和全局都有, 该听谁的
    优先级: 局部 > 全局
    
2. 局部和全局哪个好
    全局的好处在于无需重复写代码, 但是跳转的页面却很单一
    局部的好处在于不同的视图函数在用户没有登录的情况下可以跳转到不同的页面    
"""

# @login_required(login_url='/app08/login')  # 局部配置: 用户没有登录跳转到login_url指定的页面
@login_required  # 全局配置: 在settings中配置LOGIN_URL = '/app08/login/'
def home(request):
    """用户登陆之后才能看home"""
    print(request.user)  # 用户对象  AnonymousUser匿名用户
    # 判断用户是否登录
    print(request.user.is_authenticated)
    # 自动去django_session里面查找对应的用户对象给你封装到request.user中
    return HttpResponse('OK')

@login_required
def set_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        # 先校验两次密码是否一致
        if new_password == confirm_password:
            # 校验老密码对不对
            is_correct = request.user.check_password(old_password)  # 自动加密, 比对密码
            if is_correct:
                # 修改密码
                request.user.set_password(new_password) # 仅仅是在修改对象的属性
                request.user.save()  # 这一步才是真正的操作数据库

        return redirect('/app08/login')
    return render(request, 'app08/set_password.html', locals())

@login_required
def logout(request):
    auth.logout(request)  # 类似于request.session.flush()
    return redirect('/app08/login/')

from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 操作auth_user表写入数据
        # User.objects.create(username=username, password=password)  # 写入数据, 不能用create, 密码没有加密处理
        # 创建普通用户
        User.objects.create_user(username=username, password=password)
        # 创建超级用户(了解)
        # User.objects.create_superuser(username=username, password=password)
    return render(request, 'app08/register.html')