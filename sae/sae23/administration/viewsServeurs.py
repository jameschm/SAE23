from django.shortcuts import render
from .forms import serveursForm, types_serveursForm
from . import models
from django.http import HttpResponseRedirect
from django.conf import settings
import os

def affiche(request):
    base = list(models.serveurs.objects.all())
    return render(request, "administration/serveurs/affiche.html", {"base": base})

def ajout_Serveurs(request):
    if request.method == "POST":
        form = serveursForm(request)
        if form.is_valid():
            serveur = form.save()
            return render(request,"administration/Serveurs/traitement-ajout.html",{"serveur" : serveur})
        else:
            return render(request,"administration/Serveurs/ajout.html",{"form": form})
    else :
        form = serveursForm()
        return render(request,"administration/Serveurs/ajout.html",{"form" : form})

def traitement_ajout_Serveurs(request):
    form = serveursForm(request.POST)
    if form.is_valid():
        serveur = form.save()
        return render(request,"administration/Serveurs/traitement-ajout.html",{"serveur" : serveur})
    else:
        return render(request,"administration/Serveurs/ajout.html",{"form": form})

def update_Serveurs(request, id):
    serveur = models.serveurs.objects.get(pk=id)
    form = serveursForm(initial={
        'nom': serveur.nom,
        'type_serveur': serveur.types_serveurs,
        'nombre_processeur': serveur.nombre_processeur,
        'capacite_memoire': serveur.capacite_memoire,
        'capacite_stockage': serveur.capacite_stockage,
    })
    return render(request, "administration/Serveurs/update.html", {"form": form, "id": id})

def traitement_update_Serveurs(request, id):
    form = serveursForm(request.POST)
    if form.is_valid():
        serveur = form.save(commit=False)
        serveur.id = id;
        serveur.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "administration/Serveurs/update.html", {"form": form, "id": id})

def delete_Serveurs(request, id):
    serveur=models.serveurs.objects.get(pk=id)
    serveur.delete()
    return HttpResponseRedirect("/")

def detail(request, id):
    base = list(models.services.objects.filter(serveur_lancement=id))
    te=models.serveurs.objects.get(pk=id)
    route = os.path.join(settings.MEDIA_ROOT, "test.txt")
    with open(route, 'w') as destination:
        destination.write(f"Voici la fiche du serveur {te.nom}:\n\nListe des services:")
        for t in base:
            destination.write(f"\n\n{t.id}. Le service {t.nom} a été lancer le {t.date_lancement}. Il utilise {t.espace_memoire_utilise} d'espace mémoire et {t.memoire_vive_necessaire} de mémoire vive.")
    return render(request, "administration/serveurs/detail.html", {"base": base})
