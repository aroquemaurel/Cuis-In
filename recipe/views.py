#-*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from recipe.forms import AddRecipeForm
from recipe.models import Recipe


def list(request):
    recipes = Recipe.objects.all()

    return render(request, 'recipe/list.html', {'recipes': recipes})


def add(request):
    form = AddRecipeForm()
    return render(request, 'recipe/add.html', locals())


def show(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipe/show.html', {'recipe': recipe})
