from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404

# Create your views here.
def loginUser(request) : 
    return HttpResponse('Login user page')

def signupUser(request) : 
    return render(request, 'auth/signup.html')