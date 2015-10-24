from django.http import HttpResponseNotFound
from django.shortcuts import render

from recipe.models import Recipe


def search(request):
    recipes = Recipe.objects.all()
    search_text = request.GET.get('s', '')
    if search_text != '':
        recipes = recipes.filter(title__icontains=search_text)
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    
    return render(request, 'search/search.html', {'recipes': recipes})
