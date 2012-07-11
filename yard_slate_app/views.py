from django.shortcuts import render_to_response
from collections import namedtuple

def index(request):
    return render_to_response('index.html')

def create(request):
    return render_to_response('create.html')

def view_slate(request):
    slate = Slate(123)
    return render_to_response('view_slate.html', {'slate' : slate})

Slate = namedtuple('slate', ('id'))