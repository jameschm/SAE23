from django.shortcuts import render

from .forms import utilisateursForm
from . import models
from django.http import HttpResponseRedirect

def ajout_Utilisateurs(request):
    if request.method == "POST":
        form = utilisateursForm(request)
        if form.is_valid():
            utilisateur = form.save()
            return render(request,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",{"utilisateur" : utilisateur})
        else:
            return render(request,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",{"form": form})
    else :
        form = utilisateursForm()
        return render(request,"XXXXXXXXXXXXXXXXXXXXXXX",{"form" : form})

def traitement_ajout_Utilisateurs(request):
    form = utilisateursForm(request.POST)
    if form.is_valid():
        utilisateur = form.save()
        return render(request,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",{"utilisateur" : utilisateur})
    else:
        return render(request,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",{"form": form})

def update_Utilisateurs(request, id):
    utilisateur = models.utilisateurs.objects.get(pk=id)
    form = utilisateursForm(initial={
        'nom': utilisateur.nom,
        'prenom': utilisateur.prenom,
        'email': utilisateur.email
    })
    return render(request, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX", {"form": form, "id": id})

def traitement_update_Utilisateurs(request, id):
    form = utilisateursForm(request.POST)
    if form.is_valid():
        utilisateur = form.save(commit=False)
        utilisateur.id = id;
        utilisateur.save()
        return HttpResponseRedirect("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    else:
        return render(request, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", {"form": form, "id": id})

def delete_Utilisateurs(request, id):
    utilisateur=models.utilisateurs.objects.get(pk=id)
    utilisateur.delete()
    return HttpResponseRedirect("XXXXXXXXXXXXXXXXXXX")
