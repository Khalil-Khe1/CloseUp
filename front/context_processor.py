def session_processor(request):
    #print(request.user.username + " 12")
    state = False
    if(request.user.id is not None):
        state = True
    return {"logged_in" : state}