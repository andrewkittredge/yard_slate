from django.shortcuts import render_to_response, render
from django.forms import ModelForm
from collections import namedtuple
from yard_slate_app.models import YardSlate
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from io import BytesIO

from reportlab.pdfgen import canvas
from yard_slate_app.utils.qr_code import qr_url

SLATE_IDENTIFIER = 'yard_slate'
def index(request):
    return render_to_response('index.html')

def create(request):
    if request.method == 'POST':
        form = SlateForm(request.POST, request.FILES)
        if form.is_valid():
            slate = form.save()
            return HttpResponseRedirect('/view_slate/?%s=%s' % (SLATE_IDENTIFIER, slate.id))
    else:
        form = SlateForm()
    return render(request, 'create.html', {'form' : form})


    


class SlateForm(ModelForm):
    class Meta:
        model = YardSlate

def view_slate(request):
    slate = YardSlate.objects.get(id=request.REQUEST[SLATE_IDENTIFIER])
    return render_to_response('view_slate.html', 
                              {'yard_slate' : slate}, 
                              context_instance=RequestContext(request))

def printable_slate(request):
    slate = YardSlate.objects.get(id=request.REQUEST[SLATE_IDENTIFIER])
    return render_to_response('printable_slate.html',
                              {'slate' : slate,
                               'qr_url' : qr_url(slate)},
                              context_instance=RequestContext(request))
    
def yard_slate_pdf(request):
    slate = YardSlate.objects.get(id=request.REQUEST[SLATE_IDENTIFIER])
    with BytesIO() as buffer_:
    
        pdf = canvas.Canvas(buffer_)
    
        pdf.drawString(100, 100, "PDF For Slate %s" % slate.id)
        pdf.showPage()
        pdf.save()
        out_bytes = buffer_.getvalue()
        
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachement; filename=slate.pdf'
    response.write(out_bytes)
    return response
