from django.conf.urls import url
from app07 import views

urlpatterns = [
    url(r'^index/', views.index)
]