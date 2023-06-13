from django.urls import path
from . import views, viewsApplication, viewsUtilisateurs, viewsServeurs, viewsServices, viewsTypesServeurs, viewsUsageRessources


urlpatterns = [
    path('', views.index),

#APPLICATION AFFICHE
    path('affiche-application/', viewsApplication.affiche_application),
#APPLICATION AJOUT
    path('choix-ajout/',viewsApplication.choix_ajout),
    path('ajout-application/', viewsApplication.ajout_Application),
    path('ajout-application-fichier/', viewsApplication.ajout_Application_fichier),
    path('upload/',viewsApplication.upload_file),
    path('traitement-ajout-application-fichier/', viewsApplication.traitement_ajout_Application),
    path('traitement-ajout-application/', viewsApplication.traitement_ajout_Application),
#APPLICATION UPDATE
    path('update-application/<int:id>/',viewsApplication.update_Application),
    path('traitement-update-application/<int:id>/',viewsApplication.traitement_update_Application),
#APPLICATION SUPPRIMER
    path('delete-application/<int:id>/',viewsApplication.delete_Application),

#SERVEUR AFFICHE
    path('affiche-serveur/', viewsServeurs.affiche),
#SERVEUR AJOUT
    path('ajout-serveur/', viewsServeurs.ajout_Serveurs),
    path('traitement-ajout-serveur/',viewsServeurs.traitement_ajout_Serveurs),
#SERVEUR UPDATE
    path('update-serveur/<int:id>/',viewsServeurs.update_Serveurs),
    path('traitement-update-serveur/<int:id>/', viewsServeurs.traitement_update_Serveurs),
#SERVEUR SUPPRIMER
    path('delete-serveur/<int:id>/',viewsServeurs.delete_Serveurs),
#SERVEUR DETAIL
    path('detail-serveur/<int:id>/',viewsServeurs.detail),


#SERVICE AFFICHE
    path('affiche-service/', viewsServices.affiche),
#SERVICE AJOUT
    path('ajout-service/', viewsServices.ajout_Services),
    path('traitement-ajout-service/', viewsServices.traitement_ajout_Services),
#SERVICE UPDATE
    path('update-service/<int:id>/', viewsServices.update_Services),
    path('traitement-update-service/<int:id>/', viewsServices.traitement_update_Services),
#SERVICE SUPPRIMER
    path('delete-service/<int:id>/',viewsServices.delete_Services),

#TYPE SERVEUR AFFICHE
    path('affiche-type-serveur/', viewsTypesServeurs.affiche),
#TYPE SERVEUR  AJOUT
    path('ajout-type-serveur/', viewsTypesServeurs.ajout_TypesServeurs),
    path('traitement-ajout-type-serveur/',viewsTypesServeurs.traitement_ajout_TypesServeurs),
#TYPE SERVEUR UPDATE
    path('update-type-serveur/<int:id>/', viewsTypesServeurs.update_TypesServeurs),
    path('traitement-update-type-serveur/<int:id>/', viewsTypesServeurs.traitement_update_TypesServeurs),
#TYPE SERVEUR SUPPRIMER
    path('delete-type-serveur/<int:id>/',viewsTypesServeurs.delete_TypesServeurs),

#UTILISATEUR AFFICHE
    path('affiche-utilisateur/',viewsUtilisateurs.affiche),
#UTILISATEUR AJOUT
    path('ajout-utilisateur/', viewsUtilisateurs.ajout_Utilisateurs),
    path('traitement-ajout-utilisateur/',viewsUtilisateurs.traitement_ajout_Utilisateurs),
#UTILISATEUR UPDATE
    path('update-utilisateur/<int:id>/', viewsUtilisateurs.update_Utilisateurs),
    path('traitement-update-utilisateur/<int:id>/', viewsUtilisateurs.traitement_update_Utilisateurs),
#UTILISATEUR SUPPRIMER
    path('delete-utilisateur/<int:id>/',viewsUtilisateurs.delete_Utilisateurs),

]

