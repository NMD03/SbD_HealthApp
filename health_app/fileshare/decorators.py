from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator

def doctor_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'doctor':
            return view_func(request, *args, **kwargs)
        if group == 'patient':
            return redirect('index')
    return wrapper_function

def patient_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'patient':
            return view_func(request, *args, **kwargs)
        if group == 'doctor':
            return redirect('index')
    return wrapper_function