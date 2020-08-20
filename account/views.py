from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404

from bloggingproject.decorators import is_loggedin
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Follower, Notifications
from datetime import datetime

#   function to log the user in the application
@is_loggedin
def loginUser(request) : 
    if request.method == 'POST' : 
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None : 
            login(request, user)
            return redirect('/')
        else : 
            messages.error(request, 'Invalid username or password')
            return redirect('/account/login')

    else : 
        return render(request, 'auth/login.html')

#   function to render the view for signup 
@is_loggedin
def signupUser(request) : 
    return render(request, 'auth/signup.html')


#   function to log the user out
def logoutUser(request) : 
    logout(request)
    return redirect('/account/login')


#   view function to follow a user
@login_required(login_url='/account/login/')
def followUser(request) :
    if request.method == 'POST' : 
        user_from = request.user;user_to = request.POST.get("to_user")

        user_to = User.objects.get(id=user_to)
        
        if Follower.objects.filter(user_from=user_from, user_to=user_to).exists() : 
            follow = Follower.objects.get(user_from=user_from,user_to=user_to)
            follow.delete()
            return JsonResponse({
                "message" : "Follow",
                "Action Performed" : "Unfollow" 
            })
        else : 
            Follower.objects.create(user_from = user_from, user_to = user_to)
            Notifications.objects.create(user=user_to, title="{} started following you".format(user_from), time_created=datetime.now(), link="/@{}".format(user_from))
            return JsonResponse({
                "message" : "Unfollow",
                "Action Performed" : "Follow" 
            })

    else : 
        return redirect("/")


@login_required(login_url='/account/login/')
def markAsRead(request) : 
    Notifications.objects.filter(user=request.user).update(is_read = True)
    return JsonResponse({
        'counts' : 0
    })
