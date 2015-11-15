from django.shortcuts import render
from tasting.models import Tasting
from tasting.models import TastingCategory

def list(request, category='whiskies'):
    current_cat = TastingCategory.objects.get(slug=category)
    categories = TastingCategory.objects.all().order_by('title')
    tasting_list = Tasting.objects.all().filter(category=current_cat).order_by('name')
    #paginator = Paginator(recipes_list, 15)
    #page = request.GET.get('page')
    #try:
#        recipes = paginator.page(page)
 #   except PageNotAnInteger:
  #      recipes = paginator.page(1)
   # except EmptyPage:
    #    recipes = paginator.page(paginator.num_pages)

    return render(request, 'tasting/list.html', {'categories': categories,
                                                'currentCat': current_cat,
                                                'tastings': tasting_list
                                                })

"""
    paginator = Paginator(restaurants_list, 15)
    page = request.GET.get('page')
    try:
        restaurants = paginator.page(page)
    except PageNotAnInteger:
        restaurants = paginator.page(1)
    except EmptyPage:
        restaurants = paginator.page(paginator.num_pages)
"""
