from django.http import HttpResponse, HttpResponseRedirect
from django.apps import apps
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as djUser

from front.models import User
from front.src.controller.forms import UserForm

#Create views
def homepage_view(request):
    obj : User
    context = {
        'username': request.user.username
    }
    request.session["context"] = context
    return render(request, 'generic/home.html', context)

def user_create_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST or None)
        print('something')
        if "signup-submit" in request.POST:
            print('something')
            if(form.is_valid()):
                obj : User
                obj = form.save()
                u = obj.convert_user()
                login(request, u)
                return homepage_view(request)
            else:
                form = UserForm(request.POST or None)
                return render(request, 'user/signup.html', {'form': form})
                #add field checkers
    else:
        #back to signup
        form = UserForm(request.POST or None)
    return render(request, 'user/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if "login-submit" in request.POST:
            obj : User
            try:
                obj = authenticate(request, username = request.POST.get('username'), password = request.POST.get('password'))
            except User.DoesNotExist:
                obj = None
            if obj is not None:
                login(request, obj)
                return homepage_view(request)
                #return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})

def sign_out(request):
    logout(request)
    print("entered")
    return homepage_view(request)
