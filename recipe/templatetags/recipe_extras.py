# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(is_safe=True)
def star(nb_star):
    ret = ""
    for i in range(0, nb_star):
        ret += '<i class="glyphicon glyphicon-star"></i>&nbsp;'

    for i in range(nb_star, 5):
        ret += '<i class="glyphicon glyphicon-star-empty"></i>'

    return mark_safe(ret)

@register.filter(name="duration")
def duration(nb_minutes):
    hours = int(nb_minutes/60)
    minutes = nb_minutes % 60
    ret = ""

    if hours == 0:
        ret += repr(minutes)+"mn"
    else:
        ret += repr(hours)+"h"+repr(minutes)+"mn"

    return ret