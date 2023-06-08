from django.shortcuts import render

from .forms import types_serveursForm
from . import models
from django.http import HttpResponseRedirect

def ajout_TypesServeurs(request):
    if request.method == "POST":
        form = types_serveursForm(request)
        if form.is_valid():
            typeserveur = form.save()
            return render(request,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",{"typeserveur" : typeserveur})
        else:
            return render(request,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",{"form": form})
    else :
        form = types_serveursForm()
        return render(request,"XXXXXXXXXXXXXXXXXXXXXXX",{"form" : form})

def traitement_ajout_TypesServeurs(request):
    form = types_serveursForm(request.POST)
    if form.is_valid():
        typesserveur = form.save()
        return render(request,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",{"typesserveur" : typesserveur})
    else:
        return render(request,"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",{"form": form})

def update_TypesServeurs(request, id):
    typeserveur = models.types_serveurs.objects.get(pk=id)
    form = types_serveursForm(initial={
        'type': typeserveur.type,
        'description': typeserveur.description,
    })
    return render(request, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX", {"form": form, "id": id})

def traitement_update_TypesServeurs(request, id):
    form = types_serveursForm(request.POST)
    if form.is_valid():
        typeserveur = form.save(commit=False)
        typeserveur.id = id;
        typeserveur.save()
        return HttpResponseRedirect("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    else:
        return render(request, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", {"form": form, "id": id})

def delete_TypesServeurs(request, id):
    typeserveur=models.types_serveurs.objects.get(pk=id)
    typeserveur.delete()
    return HttpResponseRedirect("XXXXXXXXXXXXXXXXXXX")
