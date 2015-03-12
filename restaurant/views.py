from django.shortcuts import render
from restaurant.models import Restaurant

def list(request):
    restaurants = Restaurant.objects.all().order_by('title')

    return render(request, 'restaurant/list.html', {'restaurants': restaurants})

