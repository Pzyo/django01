from django.conf.urls import url
from app07 import views

urlpatterns = [
    url(r'^index/', views.index),

    # 转账
    url(r'^transfer/', views.transfer),
    # 钓鱼网站
    url(r'^transfers/', views.transfers),
]