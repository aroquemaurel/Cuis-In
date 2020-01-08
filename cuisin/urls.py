from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('cuisin.recipe.urls')),
    url(r'^', include('cuisin.restaurant.urls')),
    url(r'^', include('cuisin.tasting.urls')),
    url(r'^', include('cuisin.members.urls')),
    url(r'^', include('cuisin.search.urls')),
]
