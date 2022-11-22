
from django.urls import path, include
from user import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>/', views.read) #바뀔 수 있는 값 지정
]
 