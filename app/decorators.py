from django.http import HttpResponse
from django.shortcuts import redirect

    if not user.is_authenticated: 
        return redirect("must_authenticate")

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('must_authenticate')
        else:
            return view_func(request, *args, **kwargs)

    return 