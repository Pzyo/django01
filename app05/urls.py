from django.conf.urls import url
from app05 import views

urlpatterns = [
    # forms组件前戏
    url(r'^ab_form/',views.ab_form),
    # forms组件渲染标签
    url(r'^index/',views.index)
]