from django.urls import path
from . import views, viewsApplication, viewsUtilisateurs, viewsServeurs, viewsServices, viewsTypesServeurs, viewsUsageRessources

urlpatterns = [
    path('', views.index),
    path('ajout-application/', viewsApplication.ajout_Application),
    path('traitement-ajout-application/', viewsApplication.traitement_ajout_Application),

    path('ajout-serveur/', viewsServeurs.ajout_Serveurs),
    path('traitement-ajout-serveur/',viewsServeurs.traitement_ajout_Serveurs),

    path('ajout-service/', viewsServices.ajout_Services),
    path('traitement-ajout-application/', viewsServices.traitement_ajout_Services),

]