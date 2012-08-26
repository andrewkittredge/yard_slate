import dateutil.parser 

from django.shortcuts import render_to_response, render
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.forms.fields import DateTimeField

from slate_app.models import Slate
from slate_app.utils.qr_code import qr_url

SLATE_IDENTIFIER = 'id'
def index(request):
    return render_to_response('index.html')

def create(request):
    if request.method == 'POST':
        form = SlateForm(request.POST, request.FILES)
        if form.is_valid():
            slate = form.save()
            return HttpResponseRedirect('/view_slate/%s/' % (slate.id))
    else:
        form = SlateForm()
    return render(request, 'create.html', {'form' : form})

def view_slate(request, id):
    slate = Slate.objects.get(id=id)
    return render_to_response('view_slate.html', 
                              {'slate' : slate}, 
                              context_instance=RequestContext(request))

def printable_slate(request, id):
    slate = Slate.objects.get(id)
    return render_to_response('printable_slate.html',
                              {'slate' : slate,
                               'qr_url' : qr_url(slate)},
                              context_instance=RequestContext(request))
 
class FuzzyDateTimeField(DateTimeField):
    def to_python(self, value):
        try:
            date = dateutil.parser.parse(value)
        except ValueError:
            #Date utils couldn't figure it out.  Let the default parser have a
            #swing at it and throw errors as necessary.
            date = value
        return DateTimeField.to_python(self, date)

class SlateForm(ModelForm):
    start_time = FuzzyDateTimeField()
    end_time = FuzzyDateTimeField()
    class Meta:
        model = Slate

