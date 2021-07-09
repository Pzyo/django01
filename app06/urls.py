from django.conf.urls import url
from app06 import views

urlpatterns = [
    url(r'^login/',views.login),
    url(r'^home/',views.home),
    url(r'^index/',views.index),
    url(r'^func/',views.func),
]