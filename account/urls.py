from django.urls import path, re_path

from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('signup/', views.signupUser, name='signup')
]