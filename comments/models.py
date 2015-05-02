#-*- coding: utf-8 -*-
import datetime
from django.contrib.auth.models import User
from django.db import models
from recipe.models import Recipe


class Comment(models.Model):
    author = models.ForeignKey(User)
    recipe = models.ForeignKey(Recipe)
    date = models.DateTimeField()
    text = models.TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.date = datetime.datetime.now()
        super(Comment, self).save(*args, **kwargs)

