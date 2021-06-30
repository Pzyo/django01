from django.conf.urls import url
from app03 import views

urlpatterns = [
    url(r'^reg/',views.reg,name='app03_ggg'),
]