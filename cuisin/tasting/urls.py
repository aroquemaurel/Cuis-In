from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^degustations/(?P<id>\d+)-(?P<slug>.+)$', views.show, name="tasting.show"),
    url(r'^degustations/(?P<category>.+)$', views.list, name="tasting.list"),
    url(r'^degustations$', views.list, name="tasting.list"),
]
