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
    url(r'^ab_file',views.ab_file)
]