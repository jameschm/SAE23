from django.shortcuts import render
from .forms import applicationsForm
from . import models
from django.http import HttpResponseRedirect

def ajout_Application(request):
    if request.method == "POST":
        form = applicationsForm(request)
        if form.is_valid():
            application = form.save()
            return render(request,"administration/Application/traitement-ajout.html",{"application" : application})
        else:
            return render(request,"administration/Application/ajout.html",{"form": form})
    else :
        form = applicationsForm()
        return render(request,"administration/Application/ajout.html",{"form" : form})

def traitement_ajout_Application(request):
    form = applicationsForm(request.POST)
    if form.is_valid():
        application = form.save()
        return render(request,"administration/Application/traitement-ajout.html",{"application" : application})
    else:
        return render(request,"administration/Application/ajout.html",{"form": form})

def update_Application(request, id):
    application = models.applications.objects.get(pk=id)
    form = applicationsForm(initial={
        'nom': application.nom,
        'logo': application.logo,
        'serveur': application.serveur,
        'utilisateur': application.utilisateur,
    })
    return render(request, "administration/Application/update.html", {"form": form, "id": id})

def traitement_update_Application(request, id):
    form = applicationsForm(request.POST)
    if form.is_valid():
        Application = form.save(commit=False)
        Application.id = id;
        Application.save()
        return HttpResponseRedirect("")
    else:
        return render(request, "administration/Application/update.html", {"form": form, "id": id})

def delete_Application(request, id):
    application=models.applications.objects.get(pk=id)
    application.delete()
    return HttpResponseRedirect("")

