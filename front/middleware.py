from django.shortcuts import render
from django.template import Context, Template
from django.template.response import TemplateResponse

class SessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #c = RequestContext(request, {'foo': 'bar',})        
        response = self.get_response(request)
        return response