from django.http import HttpResponse, HttpResponseRedirect
from django.apps import apps
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as djUser

from front.models import User, Event
from front.src.controller.forms import UserForm, EventForm

#Create views
def homepage_view(request):
    obj : User
    return render(request, 'generic/home.html')

def user_create_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST or None)
        if "signup-submit" in request.POST:
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

def gen_form(request, entity):
    l = []
    forms = {}
    context = {}
    l.append(request)
    if request.method == 'POST':
        forms = {
            "event": EventForm(request.POST or None),
        }   

        form = forms[entity]
        context = {
            'form': form,
            'form_title': "Add " + entity
        }   
        l.append(context)

        if "generic-submit" in request.POST:
            form.instance.organizer_id = request.user.id
            if(form.is_valid()):
                form.save()
                l.append('generic/home.html')
                #return homepage_view(request)
            else:
                context["form"] = forms[entity]
                l.append('generic/generic-form.html')
                #return render(request, 'generic/generic-form.html', context)
    else:
        forms = {
            "event": EventForm(request.POST or None),
        }
        form = forms[entity]
        context["form"] = form
        l.append(context)
    l.append('generic/generic-form.html')
    return l
    #return render(request, 'generic/generic-form.html', context)
