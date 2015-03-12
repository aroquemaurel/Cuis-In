from django.shortcuts import render


def list(request):
    return render(request, 'restaurant/list.html', {'current_date': datetime.now()})

