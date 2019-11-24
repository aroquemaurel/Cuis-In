# -*- coding: utf-8 -*-
from django import template
from django.template import TemplateSyntaxError, Variable
from django.utils.safestring import mark_safe
from django.template import Library, Node, TemplateSyntaxError

register = template.Library()


#@register.filter(name='addcss')
#def addcss(field, css):
#    return field.as_widget(attrs={"class": css})


@register.filter(is_safe=True)
def star(nb_star):
    ret = ""

    for i in range(0, nb_star):
        ret += '<i class="glyphicon glyphicon-star"></i>&nbsp;'

    for i in range(nb_star, 5):
        ret += '<i class="glyphicon glyphicon-star-empty"></i>'

    if nb_star == -1:
        ret = '<i class="glyphicon glyphicon-question-sign"></i>'

    return mark_safe(ret)


@register.filter(is_safe=True)
def bool(check):
    if check:
        ret = '<i class="glyphicon glyphicon-ok"></i>'
    else:
        ret = '<i class="glyphicon glyphicon-remove"></i>'

    return mark_safe(ret)


@register.filter(name="duration")
def duration(nb_minutes):
    hours = int(nb_minutes/60)
    minutes = nb_minutes % 60
    ret = ""

    if hours == 0:
        ret += str(minutes)+"mn"
    else:
        ret += str(hours)+"h"+str(minutes)+"mn"

    return ret


@register.filter(name="hash")
def hash(h, key):
    if key in h:
        return h[key]
    else:
        return None


class RangeNode(Node):
    def __init__(self, num, context_name):
        self.num = Variable(num)
        self.context_name = context_name

    def render(self, context):
        context[self.context_name] = range(int(self.num.resolve(context)))
        return ""


@register.tag
def num_range(parser, token):
    """
    Takes a number and iterates and returns a range (list) that can be
    iterated through in templates

    Syntax:
    {% num_range 5 as some_range %}

    {% for i in some_range %}
      {{ i }}: Something I want to repeat\n
    {% endfor %}

    Produces:
    0: Something I want to repeat
    1: Something I want to repeat
    2: Something I want to repeat
    3: Something I want to repeat
    4: Something I want to repeat
    """
    try:
        fnctn, num, trash, context_name = token.split_contents()
    except ValueError:
        raise TemplateSyntaxError("%s takes the syntax %s number_to_iterate\
            as context_variable" % (fnctn, fnctn))
    if not trash == 'as':
        raise TemplateSyntaxError("%s takes the syntax %s number_to_iterate\
            as context_variable" % (fnctn, fnctn))

    return RangeNode(num, context_name)
