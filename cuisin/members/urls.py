from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^deconnexion$', views.deconnection),
    url(r'^connexion$', views.connection),
]
