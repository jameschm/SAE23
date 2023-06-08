from django.shortcuts import render

from .forms import servicesForm
from . import models
from django.http import HttpResponseRedirect

def ajout_Services(request):
    if request.method == "POST":
        form = servicesForm(request)
        if form.is_valid():
            service = form.save()
            return render(request,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",{"service" : service})
        else:
            return render(request,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",{"form": form})
    else :
        form = servicesForm()
        return render(request,"XXXXXXXXXXXXXXXXXXXXXXX",{"form" : form})

def traitement_ajout_Services(request):
    form = servicesForm(request.POST)
    if form.is_valid():
        service = form.save()
        return render(request,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",{"service" : service})
    else:
        return render(request,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",{"form": form})

def update_Serveurs(request, id):
    service = models.services.objects.get(pk=id)
    form = servicesForm(initial={
        'nom': service.nom,
        'date_lancement': service.date_lancement,
        'espace_memoire_utilise': service.espace_memoire_utilise,
        'memoire_vive_necessaire': service.memoire_vive_necessaire,
        'serveur_lancement': service.serveur_lancement,
    })
    return render(request, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX", {"form": form, "id": id})

def traitement_update_Services(request, id):
    form = servicesForm(request.POST)
    if form.is_valid():
        service = form.save(commit=False)
        service.id = id;
        service.save()
        return HttpResponseRedirect("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    else:
        return render(request, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", {"form": form, "id": id})

def delete_Services(request, id):
    service=models.services.objects.get(pk=id)
    service.delete()
    return HttpResponseRedirect("XXXXXXXXXXXXXXXXXXX")
