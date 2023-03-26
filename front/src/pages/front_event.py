from django.http import HttpResponse, HttpResponseRedirect
from django.apps import apps
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as djUser

from front.models import Event
from front.src.controller.forms import *
from front.src.pages.views import gen_form

def event_create_view(request):
    l = gen_form(request, "event")
    print(len(l))
    if len(l) > 1:
        return render(l[0], l[2], l[1])
    else:
        return render(request, l[0])
    

def dashboard_view(request):
    list_events = Event.objects.all()
    context = {
        "event_list": list_events,
    }
    return render(request, "event/event-dashboard.html", context)

def event_view(request, event_id):
    e = get_object_or_404(Event, pk=event_id)
    return render(request, "event/event.html", {"event": e})

def event_discussion(request, event_id):
    e = get_object_or_404(Event, pk=event_id)
    return render(request, "event/event-discussion.html", {"event": e})