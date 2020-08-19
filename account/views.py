from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404

from bloggingproject.decorators import is_loggedin
from django.contrib import messages

@is_loggedin
def loginUser(request) : 
    if request.method == 'POST' : 
        return JsonResponse(request.POST)
    else : 
        return render(request, 'auth/login.html')

@is_loggedin
def signupUser(request) : 
    return render(request, 'auth/signup.html')