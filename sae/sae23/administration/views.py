from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'administration/index.html')

