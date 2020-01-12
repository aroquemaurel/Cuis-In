#-*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django_unique_slugify import unique_slugify
from cuisin.tags.models import Tag


class Category(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.title)

        super(Category, self).save(**kwargs)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, default="")
    note = models.IntegerField()
    hard = models.IntegerField()
    serves = models.IntegerField()
    preparationTime = models.IntegerField()
    cuissonTime = models.IntegerField()
    preparation = models.TextField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'ajout")
    ingredients = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Recipe, self).save(*args, **kwargs)
