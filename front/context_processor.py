from django.shortcuts import get_object_or_404

def session_processor(request):
    return {
        "logged_in" : verify_login(request),
        "item_id": get_id(request)

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