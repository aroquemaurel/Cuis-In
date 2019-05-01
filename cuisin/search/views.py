from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render

from cuisin.recipe.models import Recipe
from cuisin.tags.models import Tag


def search(request):
    recipes = Recipe.objects.all()
    tags = Tag.objects.all()
    search_text = request.GET.get('s', '')
    if search_text != '':
        id_tags = tags.values_list('id').filter(tag__icontains=search_text)
        recipes_list = recipes.filter(Q(title__icontains=search_text) |Q(tags__id__in=id_tags))
        paginator = Paginator(recipes_list, 15)
        page = request.GET.get('page')
        try:
            recipes = paginator.page(page)
        except PageNotAnInteger:
            recipes = paginator.page(1)
        except EmptyPage:
            recipes = paginator.page(paginator.num_pages)

    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    
    return render(request, 'search/search.html', {'recipes': recipes, 's':search_text})
