# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
def tag(ptag):
    ret = '<i class="label label-info">'+ptag+'</i>'

    return mark_safe(ret)
