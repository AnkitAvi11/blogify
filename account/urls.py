from django.urls import path, re_path

from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('signup/', views.signupUser, name='signup'),
    path('logout/', views.logoutUser, name='logout'),
    path('followUser/', views.followUser, name='followuser'),
    path('markasread/', views.markAsRead, name='markread'),
    
]