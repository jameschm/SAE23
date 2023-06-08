from django.shortcuts import render

from .forms import usage_ressourcesForm
from . import models
from django.http import HttpResponseRedirect

def ajout_UsageRessources(request):
    if request.method == "POST":
        form = usage_ressourcesForm(request)
        if form.is_valid():
            usageressource = form.save()
            return render(request,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",{"usageressource" : usageressource})
        else:
            return render(request,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",{"form": form})
    else :
        form = usage_ressourcesForm()
        return render(request,"XXXXXXXXXXXXXXXXXXXXXXX",{"form" : form})

def traitement_ajout_UsageRessources(request):
    form = usage_ressourcesForm(request.POST)
    if form.is_valid():
        usageressource = form.save()
        return render(request,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",{"usageressource" : usageressource})
    else:
        return render(request,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",{"form": form})

def update_UsagesRessources(request, id):
    usageressource = models.usage_ressources.objects.get(pk=id)
    form = usage_ressourcesForm(initial={
        'application': usageressource.application,
        'service': usageressource.service,
    })
    return render(request, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX", {"form": form, "id": id})

def traitement_update_UsagesRessources(request, id):
    form = usage_ressourcesForm(request.POST)
    if form.is_valid():
        usageressource = form.save(commit=False)
        usageressource.id = id;
        usageressource.save()
        return HttpResponseRedirect("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    else:
        return render(request, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", {"form": form, "id": id})

def delete_UsagesRessources(request, id):
    usageressource=models.usage_ressources.objects.get(pk=id)
    usageressource.delete()
    return HttpResponseRedirect("XXXXXXXXXXXXXXXXXXX")
