from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^degustations/(?P<id>\d+)-(?P<slug>.+)$', views.show),
    url(r'^degustations/(?P<category>.+)$', views.list),
    url(r'^degustations$', views.list),
]
