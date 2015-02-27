#-*- coding: utf-8 -*-
from _ast import Add

from django.shortcuts import render, get_object_or_404
from recipe.forms import AddRecipeForm
from recipe.models import Recipe, Category


def list(request, category='entree'):
    current_cat = Category.objects.get(slug=category)
    categories = Category.objects.all()
    recipes = Recipe.objects.all().filter(category=current_cat)

    return render(request, 'recipe/list.html', {'categories': categories,
                                                'currentCat': current_cat,
                                                'recipes': recipes})


def add(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)

        form.save()
    else:
        form = AddRecipeForm()

    return render(request, 'recipe/add.html', locals())


def show(request, id, slug):
    recipe = get_object_or_404(Recipe, id=id)
    categories = Category.objects.all()
    ingredients = recipe.ingredients.splitlines()

    return render(request, 'recipe/show.html', {'recipe': recipe,
                                                'categories': categories,
                                                'currentCat': recipe.category,
                                                'ingredients': ingredients
                                                })
