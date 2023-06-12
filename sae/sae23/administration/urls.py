from django.urls import path
from . import views, viewsApplication, viewsUtilisateurs, viewsServeurs, viewsServices, viewsTypesServeurs, viewsUsageRessources


urlpatterns = [
    path('', views.index),
    path('affiche-application/', viewsApplication.affiche_application),
    path('ajout-application/', viewsApplication.ajout_Application),
    path('ajout-application-fichier/', viewsApplication.ajout_Application_fichier),
    path('upload/', viewsApplication.upload_file),
    path('traitement-ajout-application-fichier/', viewsApplication.traitement_ajout_Application),
    path('traitement-ajout-application/', viewsApplication.traitement_ajout_Application),
    path('update-application/<int:id>/',viewsApplication.update_Application),
    path('traitement-update/<int:id>/',viewsApplication.traitement_update_Application),
    path('delete/<int:id>/',viewsApplication.delete_Application),
    path('upload/',viewsApplication.upload_file),
    path('choix-ajout/',viewsApplication.choix_ajout),
    path('test/',viewsApplication.test),


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


    path('ajout-type-serveur/', viewsTypesServeurs.ajout_TypesServeurs),
    path('traitement-ajout-type/',viewsTypesServeurs.traitement_ajout_TypesServeurs),

    path('ajout-util/', viewsUtilisateurs.ajout_Utilisateurs),
    path('traitement-ajout-util/',viewsUtilisateurs.traitement_ajout_Utilisateurs),
    path('affiche-util/',viewsUtilisateurs.affiche),
    path('affiche-service/',viewsServices.affiche),
]

