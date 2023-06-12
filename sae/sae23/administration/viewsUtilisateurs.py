from django.shortcuts import render

from .forms import utilisateursForm
from . import models
from django.http import HttpResponseRedirect

def ajout_Utilisateurs(request):
    if request.method == "POST":
        form = utilisateursForm(request)
        if form.is_valid():
            utilisateur = form.save()
            return render(request,"administration/utilisateurs/traitement-ajout.html",{"utilisateur" : utilisateur})
        else:
            return render(request,"administration/utilisateurs/ajout.html",{"form": form})
    else :
        form = utilisateursForm()
        return render(request,"administration/utilisateurs/ajout.html",{"form" : form})

def traitement_ajout_Utilisateurs(request):
    form = utilisateursForm(request.POST)
    if form.is_valid():
        utilisateur = form.save()
        return render(request,"administration/utilisateurs/traitement-ajout.html",{"utilisateur" : utilisateur})
    else:
        return render(request,"administration/utilisateurs/ajout.html",{"form": form})

def update_Utilisateurs(request, id):
    utilisateur = models.utilisateurs.objects.get(pk=id)
    form = utilisateursForm(initial={
        'nom': utilisateur.nom,
        'prenom': utilisateur.prenom,
        'email': utilisateur.email
    })
    return render(request, "administration/Utilisateurs/update.html", {"form": form, "id": id})

def traitement_update_Utilisateurs(request, id):
    form = utilisateursForm(request.POST)
    if form.is_valid():
        utilisateur = form.save(commit=False)
        utilisateur.id = id;
        utilisateur.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "administration/utilisateurs/update.html", {"form": form, "id": id})

def delete_Utilisateurs(request, id):
    utilisateur=models.utilisateurs.objects.get(pk=id)
    utilisateur.delete()
    return HttpResponseRedirect("/")

def affiche(request):
    base = list(models.utilisateurs.objects.all()) # méthode pour récupérer les données dans la base avec un id donnée
    return render(request,"administration/utilisateurs/affiche.html",{"base": base})

