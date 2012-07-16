from django.shortcuts import render_to_response, render
from django.forms import ModelForm
from collections import namedtuple
from yard_slate_app.models import YardSlate
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render_to_response('index.html')

def create(request):
    if request.method == 'POST':
        form = SlateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/view_slate/')
    else:
        form = SlateForm()
    return render(request, 'create.html', {'form' : form})
    


class SlateForm(ModelForm):
    class Meta:
        model = YardSlate

def view_slate(request):
            
    return render(request, 'view_slate.html')
    


Slate = namedtuple('slate', ('id'))