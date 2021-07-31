from django.conf.urls import url
from app08 import views

urlpatterns = [
    # 登录功能
    url(r'^login/', views.login),
    # 主页
    url(r'^home/', views.home),
    # 修改密码
    url(r'^set_password', views.set_password),
    # 注销功能
    url(r'^logout/', views.logout),
    # 注册功能
    url(r'^register/', views.register),
]