#-*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)

    def __unicode__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, default="")
    note = models.IntegerField(max_length=2)
    hard = models.IntegerField(max_length=2)
    serves = models.IntegerField(max_length=2)
    preparationTime = models.IntegerField(max_length=4)
    cuissonTime = models.IntegerField(max_length=4)
    preparation = models.TextField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'ajout")
    ingredients = models.TextField()

    category = models.ForeignKey('Category')


    def __unicode__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Recipe, self).save(*args, **kwargs)
