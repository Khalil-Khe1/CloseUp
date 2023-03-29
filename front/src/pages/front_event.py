from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.apps import apps
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as djUser
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string

from front.models import Event, Discussion, Node
from front.src.controller.forms import *
from front.src.pages.views import gen_form

def event_create_view(request):
    l = gen_form(request, "event")
    print(len(l))
    if len(l) > 1:
        return render(l[0], l[2], l[1])
    else:
        return render(request, l[0])

@csrf_exempt
def comment_create_view(request):
    l = gen_form(request, "discussion")
    if len(l) > 1:
        print(len(l))
        render(l[0], l[2], l[1])
        return comment_generate_temp_display(request, l[3])
    else:
        return render(request, l[0])

def comment_generate_temp_display(request, cid):
        d = get_object_or_404(Discussion, pk=cid)
        if d is not None:
            return render (request, "event/comment-display.html", {"c": d}) 

def comment_view(request, event_id):
    e = get_object_or_404(Event, pk=event_id)
    return render(request, 'generic/add-comment.html', {"event": e})

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
    print(e.id)
    disc = Discussion.objects.all().filter(event_id=event_id)
    return render(request, "event/event-discussion.html", {"event": e, "discussions": disc})

def event_discussion_details(request, event_id, post_id):
    e = get_object_or_404(Event, pk=event_id)
    d = Node.newNode(Discussion.objects.get(id=post_id))
    get_comment_children(d)
    n = Node.newNode(10)
    return render(request, "event/event-discussion-details.html", {"event": e, "postNode": d})

def get_comment_children(parent : Node):
    comment = Discussion.objects.all().filter(parent_id=parent.key.id, item_type="comment")
    for i in comment:
        ch = Node.newNode(i)
        print(ch.key.content)
        get_comment_children(ch)
        (parent.child).append(ch)
