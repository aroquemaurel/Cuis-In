#-*- coding: utf-8 -*-
from datetime import datetime

from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from cuisin.comments.forms import AddCommentForm
from cuisin.members.models import UserInfo
from cuisin.recipe.models import Recipe, Category
from cuisin.comments.models import Comment


def home(request, errors=[], category='entree'):
    current_cat = Category.objects.get(slug=category)
    categories = Category.objects.all()
    recipes_list = Recipe.objects.all().filter(category=current_cat).order_by('title')
    paginator = Paginator(recipes_list, 15)
    page = request.GET.get('page')
    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        recipes = paginator.page(1)
    except EmptyPage:
        recipes = paginator.page(paginator.num_pages)

    return render(request, 'recipe/list.html', {'categories': categories,
                                                'currentCat': current_cat,
                                                'recipes': recipes,
                                                'errors': errors})

@permission_required('recipe.add_recipe')
def add(request):
    valid = ""
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)

        if form.is_valid():
            form.save()
            valid = "ok"
        else:
            valid = "ko"
    else:
        form = AddRecipeForm()

    return render(request, 'recipe/add.html', {'form': form, 'validation': valid})


def show(request, id, slug='a'):
    recipe = get_object_or_404(Recipe, id=id)
    categories = Category.objects.all()
    ingredients = recipe.ingredients.splitlines()
    comments = Comment.objects.filter(recipe=recipe).order_by('-date')

    if request.method == 'POST':
        form = AddCommentForm(request.POST)

        if form.is_valid():
            comment = Comment()
            comment.text = form.cleaned_data['text']
            comment.author = UserInfo.objects.get(user=request.user)
            comment.recipe = recipe
            comment.date = datetime.now()
            comment.save()
    else:
        form = AddCommentForm()

    return render(request, 'recipe/show.html', {'form': form,
                                                'recipe': recipe,
                                                'categories': categories,
                                                'currentCat': recipe.category,
                                                'ingredients': ingredients,
                                                'comments': comments
                                                })
