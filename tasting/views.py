from django.shortcuts import render
from django.shortcuts import render_to_response
from tasting.models import Tasting, Coffee, Whisky, Wine
from tasting.models import TastingCategory

def list(request, category='whiskies'):
    current_cat = TastingCategory.objects.get(slug=category)
    categories = TastingCategory.objects.all().order_by('title')

    if category == 'cafes':
        tasting_list = Coffee.objects.all().order_by('name')
    elif category == 'whiskies':
        tasting_list = Whisky.objects.all().order_by('name')
    elif category == 'vins':
        tasting_list = Wine.objects.all().order_by('name')
    else:
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


def show(request, id, slug='a'):
    return render_to_response('tasting/show.html')