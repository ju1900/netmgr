from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    path('testcase/', views.testcase, name='testcase'),
]