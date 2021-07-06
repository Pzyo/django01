"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views
# from app02 import urls as app02_urls
# from app03 import urls as app03_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'index/',views.index),
    # 登录功能
    url(r'^login/',views.login),
    # 注册功能
    url(r'^register/',views.reg),
    # 展示用户列表
    url(r'^userlist/',views.userlist),
    # 编辑用户
    url(r'^edit_user/',views.edit_user),
    # 删除用户
    url(r'^delete_user/',views.delete_user),

    # 路由匹配
    # url(r'test',views.test),     # /testadd也会匹配上
    # url(r'testadd',views.testadd),
    # url(r'test/',views.test),    # asdasdtest/会匹配上
    # url(r'testadd/',views.testadd),
    # url(r'^test/',views.test),   # test/test/asdasd会匹配上
    # url(r'^testadd/',views.testadd),
    # url(r'^test/$',views.test),    # 只匹配test/
    # url(r'^testadd/$',views.testadd),

    # 首页
    url(r'^$',views.home),
    # 尾页(了解, 有漏洞)
    # url(r'',views.error),

    # 无名分组
    # url(r'^test/[0-9]{4}/',views.test),  # 匹配test/2021/
    url(r'^test/(\d+)/',views.test),

    # 有名分组
    url(r'^testadd/(?P<year>\d+)/',views.testadd),

    # 无名有名混用 不能混用
    # url(r'^index/(\d+)/(?P<year>\d+)/',views.index),

    # 单个的分组可以使用多次
    # url(r'^index/(\d+)/(\d+)/(\d+)/',views.index),
    url(r'^index/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/',views.index),

    # 反向解析
    # url(r'^func/',views.func),
    url(r'^func_k/',views.func,name='ooo'),

    # 无名分组反向解析
    url(r'^index2/(\d+)/',views.index2,name='xxx'),

    # 有名分组反向解析
    url(r'^func/(?P<year>\d+)/',views.func2,name='sss'),

    # 路由分发
    # url(r'^app02/',include(app02_urls)),  # 只要url前缀是app02开头, 全都交给app02处理
    # url(r'^app03/',include(app03_urls)),
    # 简便写法 该写法无需导入from app02 import urls as app02_urls  (推荐)
    # url(r'^app02/',include('app02.urls',namespace='app02')),
    # url(r'^app03/',include('app03.urls',namespace='app03')),
    # 注意事项, 总路由的url不能加$结尾

    url(r'^app02/',include('app02.urls')),
    url(r'^app03/',include('app03.urls')),
    url(r'^app04/',include('app04.urls')),

]

"""
index2/数字/
reverse('xxx') 报错, 还需要指定一个参数能够被\d+匹配到
"""
