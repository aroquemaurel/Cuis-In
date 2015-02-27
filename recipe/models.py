#-*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title

class Recipe(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    note = models.IntegerField(max_length=2)
    hard = models.IntegerField(max_length=2)
    serves = models.IntegerField(max_length=2)
    preparationTime = models.IntegerField(max_length=4)
    cuissonTime = models.IntegerField(max_length=4)
    preparation = models.TextField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'ajout")

    category = models.ForeignKey('Category')
    ingredients = models.ManyToManyField(Ingredient)

    def __unicode__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que nous
        traiterons plus tard et dans l'administration
        """
        return self.title

