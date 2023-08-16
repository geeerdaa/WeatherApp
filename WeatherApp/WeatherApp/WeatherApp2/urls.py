from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('info/', views.info),
    path('main/', views.main),
]