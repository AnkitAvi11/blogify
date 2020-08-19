from django.shortcuts import redirect

def is_loggedin(viewfunction) : 
    def wrapperFunction(request, *args, **kwargs) : 
        if request.user.is_authenticated : 
            return redirect('/')
        return viewfunction(request, *args, **kwargs)
        
    return wrapperFunction