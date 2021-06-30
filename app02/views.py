from django.shortcuts import render,HttpResponse,reverse,redirect

# Create your views here.
def reg(request):
    # print(reverse('ggg'))
    # 名称空间解析
    # print(reverse('app02:ggg'))
    print(reverse('app02_ggg'))
    return HttpResponse('app02/reg')

def index(request):
    # return HttpResponse('')  # 符合
    # return render(request,'home.html')  # 符合
    """
    def render(request, template_name, context=None, content_type=None, status=None, using=None):
    content = loader.render_to_string(template_name, context, request, using=using)
    return HttpResponse(content, content_type, status)
    """
    # return redirect()  # 符合

    from django.template import Template,Context
    res = Template('<h1>{{ user }}</h1>')
    con = Context({'user':{'username':'pzyo','password':'123'}})
    ret = res.render(con)
    print(ret)
    return HttpResponse(ret)

import json
from django.http import JsonResponse
def ab_json(request):
    # user_dict = {'username':'pzyo','password':'123','hobby':'girl'}
    user_dict = {'username':'pzyo你好呀','password':'123','hobby':'girl'}

    l = [111,222,333,444]

    # 先转成json格式的字符串
    # json_str = json.dumps(user_dict)
    # json_str = json.dumps(user_dict,ensure_ascii=False)  # ensure_ascii=False可以禁止将中文转为Unicode编码
    # 将该字符串返回
    # return HttpResponse(json_str)

    # 读源码掌握用法
    # return JsonResponse(user_dict,json_dumps_params={'ensure_ascii':False})

    # In order to allow non-dict objects to be serialized set the safe parameter to False.
    # return JsonResponse(l)
    return JsonResponse(l, safe=False)

def ab_file(request):
    if request.method == 'POST':
        print(request.body)  # 原生的浏览器发过来的二进制数据
        # print(request.POST)  # 只能获取普通的键值对数据 文件不行
        print(request.FILES)  # 获取文件数据
        # < MultiValueDict: {'file': [ < InMemoryUploadedFile: jenkins.png(image / png) >]} >
        # file_obj = request.FILES.get('file')  # 文件对象
        # print(file_obj.name)
        # with open(file_obj.name,'wb') as f:
        #     for line in file_obj.chunks():  # 推荐加上chunks方法 其实跟不加是一样的, 都是一行行的读
        #         f.write(line)

    # http://127.0.0.1:8000/app02/ab_file/?username=pzyo
    print(request.path)            # /app02/ab_file/
    print(request.path_info)       # /app02/ab_file/
    print(request.get_full_path()) # /app02/ab_file/?username=pzyo

    return render(request,'app02/form.html')

# from django.views import View
# class MyLogin(View):
#     def get(self,request):
#         return render(request,'app02/form.html')
#
#     def post(self,request):
#         return HttpResponse('post方法')

from django.views import View
class MyLogin(View):
    def get(self,request):
        return render(request,'app02/login.html')

    def post(self,request):
        return HttpResponse('post请求')

def index2(request):
    # 模板语法可以传递的后端数据类型
    n = 123
    f = 11.11
    s = '你好呀'
    b = False
    l = ['小红','小明','小刚','敏敏','欣欣']
    t = (111,222,333,444)
    d = {'username':'pzyo','age':18,'info':'这个人有点东西','hobby':[111,222,333,{'info':'NB'}]}
    se = {'静静','洋洋','嘤嘤'}
    lll = []
    def func():
        print('我被执行了')
        return '你的另一半在等你'

    class MyClass(object):
        def get_self(self):
            return 'self'

        @staticmethod
        def get_func():
            return 'func'

        @classmethod
        def get_class(cls):
            return 'cls'

        # 对象被展示到html页面 就类似于执行了打印操作也会触发__str__方法
        def __str__(self):
            return '到底会不会'

    obj = MyClass()

    file_size = 1231231
    import datetime
    current_time = datetime.datetime.now()

    info = '阿斯顿 全文 千万人千 万人 气温将 强化科技 后前往科 和口腔 今晚和 空间 求好玩'
    egl = 'my name is pzyo my age is 23 and i am from china'

    msg = 'I Love You and You?'
    hhh = '<h1>敏敏</h1>'
    sss = '<script>alert(123)</script>'
    from django.utils.safestring import mark_safe
    res = mark_safe('<h1>欣欣</h1>')

    # return render(request,'app02/index2.html',{}}) 一个个传
    return render(request,'app02/index2.html',locals())

def home(request):
    return render(request,'app02/home.html')

def loginn(request):
    return render(request,'app02/loginn.html')

def regn(request):
    return render(request,'app02/reg.html')