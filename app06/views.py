from django.shortcuts import render,redirect,HttpResponse

# 校验用户是否登录的装饰器
"""
用户如果在没有登录的情况下想访问一个需要登录的页面
那么先跳转到登录页面 当用户输入正确的用户名和密码后
应该跳转到用户之前想要访问的页面去 而不是应该直接写死
"""
def login_auth(func):
    def inner(request, *args, **kwargs):
        # print(request.path_info)
        # print(request.get_full_path())  # 能够获取到用户上次想访问的url
        target_url = request.get_full_path()
        if request.COOKIES.get('username'):
            return func(request, *args, **kwargs)
        else:
            return redirect('/app06/login/?next=%s'%target_url)
    return inner

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'pzyo' and password == '123':
            # 获取用户上次想要访问的url
            target_url = request.GET.get('next')  # 这个结果可能是null
            if target_url:
                obj = redirect(target_url)
            else:
                # 保存用户登录状态
                obj = redirect('/app06/home/')
            # 让浏览器记录cookie数据
            obj.set_cookie('username','pzyo666')
            """
            浏览器不单单会帮你存
            而且后面每次访问你的时候还会带着它过来
            """
            # 跳转到一个需要用户登录后才能看到的页面
            return obj
    return render(request, 'app06/login.html')

@login_auth
def home(request):
    # 获取cookie信息  判断有没有
    # if request.COOKIES.get('username') == 'pzyo666':
    #     return HttpResponse('我是home页面, 只有登录用户才能看到')
    # # 没有登录应该跳转到登录页面
    # return redirect('/app06/login')
    return HttpResponse('我是home页面, 只有登录用户才能看到')

@login_auth
def index(request):
    return HttpResponse('我是index页面, 只有登录用户才能看到')

@login_auth
def func(request):
    return HttpResponse('我是func页面, 只有登录用户才能看到')
