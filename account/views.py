from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404

from bloggingproject.decorators import is_loggedin
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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