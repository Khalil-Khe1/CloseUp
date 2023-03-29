from django.http import HttpResponse, HttpResponseRedirect
from django.apps import apps
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as djUser
from django.views.decorators.csrf import csrf_exempt

from front.models import User, Event, Discussion
from front.src.controller.forms import UserForm, EventForm, DiscussionForm

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
    else:
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
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})

def sign_out(request):
    logout(request)
    print("entered")
    return homepage_view(request)

@csrf_exempt
def gen_form(request, entity):
    l = []
    forms = {}
    forms_before = {
        "event": EventForm(request.POST or None),
        "discussion": DiscussionForm(request.POST or None)
    }
    context = {}
    l.append(request)
    if request.method == 'POST':
        forms = forms_before 
        form = forms[entity]
        context = {
            'form': form,
            'form_title': "Add " + entity
        }   
        l.append(context)
        print(request.POST)
        if "generic-submit" in request.POST:
            spec_form_cases(request, form, entity)
            if(form.is_valid()):
                gen_info = form.save()
                print("state")                
                l.append('generic/home.html')
                l.append(gen_info.id)                
            else:
                context["form"] = forms[entity]
                l.append('generic/generic-form.html')
    else:
        forms = forms_before
        form = forms[entity]
        context["form"] = form
        l.append(context)
        l.append('generic/generic-form.html')
    return l

def spec_form_cases(request, form, entity : str):
    if(entity == "event"):
        form.instance.organizer_id = request.user.id
    elif(entity == "discussion"): 
            form.instance.user_id = request.user.id
            form.instance.parent_id = request.POST["parent_id"]