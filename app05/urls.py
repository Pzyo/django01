from django.conf.urls import url
from app05 import views

urlpatterns = [
    # form组件前戏
    url(r'^ab_form/',views.ab_form),
]