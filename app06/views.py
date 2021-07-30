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
            obj.set_cookie('username','pzyo666',max_age=30,expires=30)
            # 超时时间3秒到期
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

@login_auth
def logout(request):
    obj = redirect('/app06/login')
    obj.delete_cookie('username')
    return obj

def set_session(request):
    request.session['hobby'] = 'girl'
    # request.session['hobby1'] = 'girl1'
    # request.session['hobby2'] = 'girl2'
    # request.session['hobby3'] = 'girl3'
    request.session.set_expiry(0)
    """
    内部发生了哪些事
        1. django内部会自动帮你生成一个随机字符串
        2. django内部自动将随机字符串和对应的数据存储到django_session表中(这一步不是直接操作的)
            2.1 先在内存中产生操作数据的缓存
            2.2 在响应结果django中间件的时候才真正的操作数据库
            ('django.contrib.sessions.middleware.SessionMiddleware')
        3. 将产生的随机字符串返回给客户端浏览器保存
    """
    return HttpResponse('嘿嘿嘿')

def get_session(request):
    # print(request.session.get('hobby'))
    if request.session.get('hobby'):
        print(request.session)
        print(request.session.get('hobby'))
        print(request.session.get('hobby1'))
        print(request.session.get('hobby2'))
        print(request.session.get('hobby3'))
        """
        内部发生了哪些事
            1. 自动从浏览器请求中获取sessionid对应的随机字符串
            2. 拿着该随机字符串去django_session表中查找对应的数据
            3. 
                如果比对上了, 则将对应的数据取出并以字典的形式封装到request.session中
                如果比对不上, 则request.session返回的是None
        """
        return HttpResponse("哈哈哈")
    return HttpResponse('大爷, 关门了')

def del_session(request):
    request.session.delete()
    return HttpResponse('删喽')


from django.views import View
from django.utils.decorators import method_decorator

"""
CBV中django不建议你直接给类的方法加装饰器
无论该装饰器能否正常工作, 都不建议直接加
"""

# @method_decorator(login_auth, name='get')  # 方式2(可以添加多个, 针对不同的方法加不同的装饰器)
# @method_decorator(login_auth, name='post')
class MyLogin(View):
    @method_decorator(login_auth)  # 方式3  它会直接作用于当前类里所有的方法
    def dispatch(self, request, *args, **kwargs):
        """
        看CBV源码可以得出, CBV里面所有的方法在执行前后需要先经过
        dispatch方法(该方法可以看成一个分发方法)
        """
        super().dispatch(request, *args, **kwargs)

    # @method_decorator(login_auth)  # 方式1
    def get(self, request):
        return HttpResponse('get请求')

    def post(self, request):
        return HttpResponse('post请求')