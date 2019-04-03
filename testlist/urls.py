from django.conf.urls import include, url
from django.urls import path
from . import views

# urlpatterns = [
#     path('product/<int:id>/', views.product),
#     path('chapter/<int:id>/', views.chapter),
#     path('testcase/', views.testcase),
#     path('', views.testlist),
# ]

urlpatterns = [
    path('product/p<int:id>/', views.product),
    path('chapter/c<int:id>/', views.chapter),
    path('section/s<int:id>/', views.section),
    path('testcase/t<int:id>/', views.testcase),
    path('', views.testlist),
]