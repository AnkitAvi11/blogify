from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.indexPage, name='home'),
    re_path(r'^@(?P<username>[a-zA-Z0-9\.\-\_\@]+)/$', views.viewUser, name='view_user'),
]