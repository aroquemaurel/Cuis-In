#-*- coding: utf-8 -*-
import datetime
from django.db import models
from cuisin.members.models import UserInfo
from cuisin.recipe.models import Recipe


class Comment(models.Model):
    author = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date = models.DateTimeField()
    text = models.TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.date = datetime.datetime.now()
        super(Comment, self).save(*args, **kwargs)

