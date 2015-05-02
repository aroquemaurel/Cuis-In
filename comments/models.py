#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from recipe.models import Recipe


class Comments:
    author = models.ForeignKey(User)
    recipe = models.ForeignKey(Recipe)
    date = models.DateTimeField()
    comment = models.TextField()
