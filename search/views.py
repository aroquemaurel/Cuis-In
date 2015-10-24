from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render

from recipe.models import Recipe
from tags.models import Tag


def search(request):
    recipes = Recipe.objects.all()
    tags = Tag.objects.all()
    search_text = request.GET.get('s', '')
    if search_text != '':
        id_tags = tags.values_list('id').filter(tag__icontains=search_text)
        recipes = recipes.filter(Q(title__icontains=search_text) |Q(tags__id__in=id_tags))
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    
    return render(request, 'search/search.html', {'recipes': recipes})
