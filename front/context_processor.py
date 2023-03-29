from django.shortcuts import get_object_or_404
from front.models import User

def session_processor(request):
    return {
        "logged_in" : verify_login(request),
        "item_id": get_id(request),
        "current_id": get_current_user(request),
        }

def verify_login(request):
    state = False
    if(request.user.id is not None):
        state = True
    return state

def get_id(request):
    path = request.get_full_path()
    if "id" in path:
        path = path[path.index("id_")+3:path.index("id_")+4:1]
    else:
        path = ""
    return path

def get_current_user(request):
    if(request.user.id is not None):
        return request.user.id
    return "-1"

def get_user(request):
    if "some_user_id" in request.POST:
        return User.objects.get(id=int(request.POST["some_user_id"]))