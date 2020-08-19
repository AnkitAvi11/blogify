from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.
def indexPage(request) : 
    if request.user.is_authenticated : 
        return render(request, './index.html')
    else : 
        return render(request, './index.html')

def viewUser(request, username) : 
    try : 
        UserModel = get_user_model()
        user = UserModel.objects.get(username=username)
        
        return render(request, './user/profile.html', {
            'user_data' : user
        })

    except UserModel.DoesNotExist : 
        raise Http404()


