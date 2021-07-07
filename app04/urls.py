from django.conf.urls import url
from app04 import views

urlpatterns = [
    # ajax相关
    url(r'ab_ajax',views.ab_ajax),
    # 前后端传输数据编码格式研究
    url(r'^index/',views.index),
    # ajax发送json格式数据
    url(r'^ab_json/',views.ab_json),
    # ajax发送文件
    url(r'^ab_file/',views.ab_file),
    # 序列化组件相关
    url(r'^ab_ser/',views.ab_ser),

    # 用户展示页
    url(r'^user/list',views.user_list),
    url(r'^delete/user/',views.delete_user),
]