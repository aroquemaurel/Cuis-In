#-*- coding: utf-8 -*-

from datetime import datetime
from django.shortcuts import render


def list(request):
    return render(request, 'recipe/list.html', {'current_date': datetime.now()})