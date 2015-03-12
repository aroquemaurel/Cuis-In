from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cuisin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^restaurants', 'restaurant.view.list');
    url(r'^recettes/ajouter', 'recipe.views.add'),
    url(r'^$', 'recipe.views.home'),
    url(r'^recettes/(?P<id>\d+)-(?P<slug>.+)$', 'recipe.views.show'),
    url(r'^recettes/(?P<category>.+)$', 'recipe.views.home'),

    url(r'^deconnexion$', 'members.views.deconnection'),
    url(r'^connexion$', 'members.views.connection'),
)
