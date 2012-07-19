from django.shortcuts import render_to_response, render
from django.forms import ModelForm
from collections import namedtuple
from yard_slate_app.models import YardSlate
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext


def index(request):
    return render_to_response('index.html')

def create(request):
    if request.method == 'POST':
        form = SlateForm(request.POST, request.FILES)
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
    slate = YardSlate.objects.get(id=1)
    return render_to_response('view_slate.html', 
                              {'yard_slate' : slate}, 
                              context_instance=RequestContext(request))

Slate = namedtuple('slate', ('id'))