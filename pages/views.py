from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from account.models import Follower

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
        
        status = "Unfollow" if Follower.objects.filter(user_from=request.user, user_to=user).exists() else "Follow"

        followers = Follower.objects.filter(user_to=user)
        followings = Follower.objects.filter(user_from=user)

        return render(request, './user/profile.html', {
            'user_data' : user,
            "status" : status,
            "followers" : followers.count(), 
            "followings" : followings.count()
        })

    except UserModel.DoesNotExist : 
        raise Http404()


