from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('recipe.views',
    # Examples:
    # url(r'^$', 'cuisin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


    url(r'^recettes/ajouter', 'add'),
    url(r'^$', 'list'),
    url(r'^recette/(?P<id>\d+)$', 'show'),
    url(r'^recettes/(?P<category>.+)$', 'list'),
)
