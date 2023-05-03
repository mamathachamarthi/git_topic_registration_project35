from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
from app.models import *

from app.forms import *

def registration(request):
    TFD=TopicForm()
    WFD=WebpageForm()
    ARFD=AccessRecordForm()
    d={'TFD':TFD,'WFD':WFD,'ARFD':ARFD}

    if request.method=='POST':
        TFD=TopicForm(request.POST)
        WFD=WebpageForm(request.POST)
        ARFD=AccessRecordForm(request.POST)
        if TFD.is_valid() and WFD.is_valid() and ARFD.is_valid():  
            NSTO=TFD.save(commit=False)
            NSTO.save()
            NSWO=WFD=WFD.save(commit=False)
            NSWO.topic_name=NSTO
            NSWO.save()
            NSAO=ARFD.save(commit=False)
            NSAO.name=NSWO
            NSAO.save()
            return HttpResponse('registration is successfull')

        else:

            return HttpResponse('data in not valid')

    return render(request,'registration.html',d)
