from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class serveursForm(ModelForm):
    class Meta:
        model = models.serveurs
        fields = ('nom', 'type_serveur', 'nombre_processeur', 'capacite_memoire', 'capacite_stockage')
        labels = {
            'nom' : _('nom'),
            'type_serveur' : _('type_serveur') ,
            'nombre_processeur' : _('nombre_processeur'),
            'capacite_memoire' : _('capacite_memoire'),
            'capacite_stockage' : _('capacite_stockage'),
    }

class types_serveursForm(ModelForm):
    class Meta:
        model = models.types_serveurs
        fields = ('type', 'description')
        labels = {
            'type' : _('type'),
            'description' : _('description'),
    }

class utilisateursForm(ModelForm):
    class Meta:
        model = models.utilisateurs
        fields = ('nom', 'prenom', 'email')
        labels = {
            'nom' : _('nom'),
            'prenom' : _('prenom'),
            'email' : _('email'),
    }

class servicesForm(ModelForm):
    class Meta:
        model = models.services
        fields = ('nom', 'date_lancement', 'espace_memoire_utilise', 'memoire_vive_necessaire', 'serveur_lancement')
        labels = {
            'nom' : _('nom'),
            'date_lancement' : _('date_lancement'),
            'espace_memoire_utilise' : _('espace_memoire_utilise') ,
            'memoire_vive_necessaire' : _('memoire_vive_necessaire'),
            'serveur_lancement' : _('serveur_lancement'),
    }

class applicationsForm(ModelForm):
    class Meta:
        model = models.services
        fields = ('nom', 'logo', 'prenom', 'email', 'serveur', 'utilisateur')
        labels = {
            'nom' : _('nom'),
            'logo' : _('logo'),
            'prenom' : _('prenom') ,
            'email' : _('email'),
            'serveur' : _('serveur'),
            'utilisateur' : _('utilisateur'),
    }

class usage_ressourcesForm(ModelForm):
    class Meta:
        model = models.services
        fields = ('application', 'service')
        labels = {
            'application': _('application'),
            'service': _('service'),
    }