from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class serveurs (models.Model):
    nom = models.CharField(max_length=100)
    types_serveurs = models.ForeignKey("types_serveurs", on_delete=models.CASCADE, default=None)
    nombre_processeur =  models.IntegerField(null = False, blank= False)
    capacite_memoire =  models.IntegerField(null = False, blank= False)
    capacite_stockage =  models.IntegerField(null = False, blank= False)


    def __str__(self):
        chaine = f"{self.nom}"
        return chaine

class types_serveurs (models.Model):
    type = models.CharField(max_length=100, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        chaine = f"{self.type}"
        return chaine

class utilisateurs (models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine

class services (models.Model):
    nom = models.CharField(max_length=100, blank=False)
    date_lancement = models.DateField(blank=False, null = False)
    espace_memoire_utilise = models.IntegerField(null = False, blank= False)
    memoire_vive_necessaire = models.IntegerField(null = False, blank= False)
    serveur_lancement = models.ForeignKey("serveurs", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f""
        return chaine

class applications (models.Model):
    nom = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="logo/", default="logo/defaut.png", null=True)
    serveur = models.ForeignKey("serveurs", on_delete=models.CASCADE, default=None)
    utilisateur = models.ForeignKey("utilisateurs", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f""
        return chaine

class usage_ressources (models.Model):
    application = models.ForeignKey("applications", on_delete=models.CASCADE, default=None)
    service = models.ForeignKey("services", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f""
        return chaine
