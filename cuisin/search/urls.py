from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^recherche$', views.search),
]
