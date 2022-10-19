from django.shortcuts import render
import imp
from app.models import *

# Create your views here.
def display_topic(request):
    T=Topic.objects.all()
    d={'topics':T}
    return render(request, 'display_topic.html',d)

def display_webpage(request):
    W=Webpage.objects.all()
    d={'webpage':W}
    return render(request,'display_webpage.html',d)

def display(request):
    A=AccessRecords.objects.all()
    d={'access':A}
    return render(request,'display_access.html',d)