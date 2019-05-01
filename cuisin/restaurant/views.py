from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from restaurant.models import Restaurant


def list(request):
    restaurants_list = Restaurant.objects.all().order_by('title')
    paginator = Paginator(restaurants_list, 15)
    page = request.GET.get('page')
    try:
        restaurants = paginator.page(page)
    except PageNotAnInteger:
        restaurants = paginator.page(1)
    except EmptyPage:
        restaurants = paginator.page(paginator.num_pages)

    return render(request, 'restaurant/list.html', {'restaurants': restaurants})


def show(request, id, slug=''):
    restaurant = get_object_or_404(Restaurant, id=id)

    return render(request, 'restaurant/show.html', {'restaurant': restaurant})
