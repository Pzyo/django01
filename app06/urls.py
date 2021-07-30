from django.conf.urls import url
from app06 import views

urlpatterns = [
    url(r'^login/',views.login),
    url(r'^home/',views.home),
    url(r'^index/',views.index),
    url(r'^func/',views.func),
    # 注销功能
    url(r'^logout/', views.logout),

    # session操作
    url(r'^set_session/', views.set_session),
    url(r'^get_session/', views.get_session),
    url(r'^del_session/', views.del_session),

    # CBV添加装饰器
    url(r'^mylogin/', views.MyLogin.as_view())
]