from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^restaurants$', views.list),
    url(r'^restaurants/(?P<id>\d+)-(?P<slug>.+)$', views.show),
]
