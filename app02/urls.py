from django.conf.urls import url
from app02 import views

urlpatterns = [
    url(r'^reg/',views.reg,name='app02_ggg'),
    # 三板斧
    url(r'^index/',views.index),
    # json相关
    url(r'^ab_json/',views.ab_json),
    # 上传文件
    url(r'^ab_file/',views.ab_file),
    # CBV路由
    # url(r'^login/',views.MyLogin.as_view()),
    # 上述代码在启动django的时候就会立刻执行as_view方法
    # 等价于 url(r'^login/',views.view)  与FBV一模一样
    # CBV与FBV在路由匹配上本质是一样  都是路由  对应  函数内存地址

    # 模板语法传值
    url(r'^index2/',views.index2),

    # 模板的继承
    url(r'^home/',views.home),
    url(r'^loginn/',views.loginn),
    url(r'^regn/',views.regn),
]
"""
函数名/方法名  加括号执行优先级最高
猜测
  as_view()
    要么是被@staticmethod修饰的静态方法
    要么是被@classmethod修饰的类方法
    
    @classonlymethod
    def as_view(cls, **initkwargs):  # 类来调用, 自动将类作为参数导入cls
       ...
"""