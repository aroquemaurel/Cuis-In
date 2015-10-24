from django.shortcuts import render
from django.db.models import Q

from recipe.models import Recipe


def search(request, searchtext):
    recipes = Recipe.objects.all()
    recipes = recipes.filter(title__icontains=searchtext)
    return render(request, 'search/search.html', {'recipes': recipes})
