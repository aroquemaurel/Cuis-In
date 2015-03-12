from django.shortcuts import render, get_object_or_404
from restaurant.models import Restaurant


def list(request):
    restaurants = Restaurant.objects.all().order_by('title')

    return render(request, 'restaurant/list.html', {'restaurants': restaurants})


def show(request, id, slug=''):
    restaurant = get_object_or_404(Restaurant, id=id)

    return render(request, 'restaurant/show.html', {'restaurant': restaurant})
