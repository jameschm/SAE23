from django.shortcuts import render

from . import models
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, 'index.html')