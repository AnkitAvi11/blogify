from django.urls import path, re_path

from . import views

urlpatterns = [
    path('add/', views.add_blog, name='addblog'),
    path('', views.viewallblogs, name='allblogs'),
]