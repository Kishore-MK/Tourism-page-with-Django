from django.shortcuts import render
from .models import desties
from django.http import HttpResponse
# Create your views here.

def index(request):
    dests = desties.objects.all()
    
    return render(request, 'index.html',{'dests': dests})

