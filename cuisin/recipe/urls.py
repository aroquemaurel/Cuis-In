from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^recettes/ajouter', views.add),
    url(r'^$', views.home),
    url(r'^recettes/(?P<id>\d+)-(?P<slug>.+)$', views.show),
    url(r'^recettes/(?P<category>.+)$', views.home),
]
