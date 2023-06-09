from django.urls import path
from . import views, viewsApplication, viewsUtilisateurs, viewsServeurs, viewsServices, viewsTypesServeurs, viewsUsageRessources

urlpatterns = [
    path('', views.index),

    path('ajout-application/', viewsApplication.ajout_Application),
    path('traitement-ajout-application/', viewsApplication.traitement_ajout_Application),
    path('update-application/<int:id>/',viewsApplication.update_Application),
    path('traitement-update/<int:id>/',viewsApplication.traitement_update_Application),
    path('delete/<int:id>/',viewsApplication.delete_Application),

    path('ajout-serveur/', viewsServeurs.ajout_Serveurs),
    path('traitement-ajout-serveur/',viewsServeurs.traitement_ajout_Serveurs),
    path('update-serveur/<int:id>/',viewsServeurs.update_Serveurs),
    path('traitement-update/<int:id>/', viewsServeurs.traitement_update_Serveurs),
    path('delete/<int:id>/',viewsServeurs.delete_Serveurs),

    path('ajout-service/', viewsServices.ajout_Services),
    path('traitement-ajout-service/', viewsServices.traitement_ajout_Services),
    path('update-service/<int:id>/', viewsServices.update_Services),
    path('traitement-update/<int:id>/', viewsServices.traitement_update_Services),
    path('delete/<int:id>/',viewsServices.delete_Services),


]