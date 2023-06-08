from django.db import models

# Create your models here.
from django.db import models


class serveurs (models.Model):
    nom = models.CharField(max_length=100)
    type_serveur = models.ForeignKey("types_serveurs", on_delete=models.CASCADE, default=None)
    nombre_processeur =  models.IntegerField(null = False, blank= False)
    capacite_memoire =  models.IntegerField(null = False, blank= False)
    capacite_stockage =  models.IntegerField(null = False, blank= False)


    def __str__(self):
        chaine = f"Le serveur {self.nom} (type: {self.type}) a une capacité mémoire de {self.capacite_memoire}, une capacité de stockage de {self.capacite_stockage} et il utilise {self.nombre_processeur} processeur"
        return chaine

class types_serveurs (models.Model):
    type = models.CharField(max_length=100, blank=False)
    description = models.TextField(null=True, blank=True)

class utilisateurs (models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

class services (models.Model):
    nom = models.CharField(max_length=100, blank=False)
    date_lancement = models.DateField(blank=False, null = False)
    espace_memoire_utilise = models.IntegerField(null = False, blank= False)
    memoire_vive_necessaire = models.IntegerField(null = False, blank= False)
    serveur_lancement = models.ForeignKey("serveurs", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nom

class applications (models.Model):
    nom_de_l_application = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/')
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    serveur = models.ForeignKey("serveurs", on_delete=models.CASCADE, default=None)
    utilisateur = models.ForeignKey("utilisateurs", on_delete=models.CASCADE, default=None)

class Usage_ressources (models.Model):
    application = models.ForeignKey("applications", on_delete=models.CASCADE, default=None)
    service = models.ForeignKey("services", on_delete=models.CASCADE, default=None)
