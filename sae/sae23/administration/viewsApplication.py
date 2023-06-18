from django.shortcuts import render
from .forms import applicationsForm, serveursForm, utilisateursForm
from . import models
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
import os

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

def affiche_application(request):
    base = list(models.applications.objects.all())
    return render(request, "administration/Application/affiche.html", {"base": base})

def choix_ajout(request):
    return render(request,"administration/Application/choix-ajout.html")

def ajout_Application_fichier(request):
    return render(request, "administration/application/ajout2.html")

def traitement_ajout_Application(request):
    form = applicationsForm(request.POST, request.FILES)
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
        return HttpResponseRedirect("/")
    else:
        return render(request, "administration/Application/update.html", {"form": form, "id": id})

def delete_Application(request, id):
    application=models.applications.objects.get(pk=id)
    application.delete()
    return HttpResponseRedirect("/")


def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['fileToUpload']
        file_name = uploaded_file.name
        if is_txt_file(file_name):
            save_path = os.path.join(settings.MEDIA_ROOT, "temp.txt")
            with open(save_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            nom = str(charger_txt("administration/media/temp/administration/temp.txt", 0))
            serveur_id = int(charger_txt("administration/media/temp/administration/temp.txt", 1))
            utilisateur_id = int(charger_txt("administration/media/temp/administration/temp.txt", 2))

            # Récupérer les objets serveur et utilisateur correspondants
            serveur = models.serveurs.objects.get(pk=serveur_id)
            utilisateur = models.utilisateurs.objects.get(pk=utilisateur_id)
            application = models.applications(nom=nom, serveur=serveur, utilisateur=utilisateur)
            application.save()
            return render(request, "administration/Application/traitement-ajout.html", {"application": application})
        else:
            return render(request, "administration/Application/erreur.html")
    return render(request, "administration/Application/ajout2.html")

def is_txt_file(file_path):
        a=[]
        a=file_path.split('.')
        return a[1] == 'txt'

def charger_txt(file_path, x):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        data = [line.strip() for line in lines]
        return data[x]