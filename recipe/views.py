#-*- coding: utf-8 -*-

from datetime import datetime
from django.shortcuts import render
from recipe.forms import AddRecipeForm

def list(request):
    return render(request, 'recipe/list.html', {'current_date': datetime.now()})


def add(request):
    form = AddRecipeForm()
    return render(request, 'recipe/add.html', locals())


