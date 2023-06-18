from django.shortcuts import render

from .forms import servicesForm
from . import models
from django.http import HttpResponseRedirect, HttpResponse

def ajout_Services(request):
    if request.method == "POST":
        form = servicesForm(request)
        if form.is_valid():
            service = form.save(commit=False)
            return render(request,"administration/Services/traitement-ajout.html",{"service" : service})
        else:
            return render(request,"administration/Services/ajout.html",{"form": form})
    else :
        form = servicesForm()
        return render(request,"administration/Services/ajout.html",{"form" : form})

def traitement_ajout_Services(request):
    form = servicesForm(request.POST)
    if form.is_valid():
        service = form.save(commit=False)
        y = 0
        x = 0
        base = list(models.services.objects.filter(serveur_lancement=service.serveur_lancement))
        for i in base:
            y += i.memoire_vive_necessaire
            x += i.espace_memoire_utilise
        y += service.memoire_vive_necessaire
        x += service.espace_memoire_utilise
        serveur = models.serveurs.objects.get(pk=service.serveur_lancement.id)
        if ((y <= serveur.capacite_memoire) and (x <= serveur.capacite_stockage)):
            service = form.save()
            return render(request, "administration/Services/traitement-ajout.html", {"service": service})
        else:
            return render(request, "administration/Services/erreur.html")
    else:
        return render(request,"administration/Services/ajout.html",{"form": form})

def update_Services(request, id):
    service = models.services.objects.get(pk=id)
    form = servicesForm(initial={
        'nom': service.nom,
        'date_lancement': service.date_lancement,
        'espace_memoire_utilise': service.espace_memoire_utilise,
        'memoire_vive_necessaire': service.memoire_vive_necessaire,
        'serveur_lancement': service.serveur_lancement,
    })
    return render(request, "administration/Services/update.html", {"form": form, "id": id})

def traitement_update_Services(request, id):
    form = servicesForm(request.POST)
    if form.is_valid():
        service = form.save(commit=False)
        service.id = id;
        service.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "administration/Services/update.html", {"form": form, "id": id})

def delete_Services(request, id):
    service=models.services.objects.get(pk=id)
    service.delete()
    return HttpResponseRedirect("/")

def affiche(request):
    base = list(models.services.objects.all())
    return render(request, "administration/Services/affiche.html", {"base": base})