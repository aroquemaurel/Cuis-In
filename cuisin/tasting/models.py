from django.db import models


class TastingCategory(models.Model):
    title = models.CharField(max_length=128)
    singularTitle = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)

    def __unicode__(self):
        return self.title


class Tasting(models.Model):
    category = models.ForeignKey('TastingCategory', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=128)
    name = models.CharField(max_length=128)
    flair = models.TextField()
    mouth = models.TextField()
    color = models.TextField()
    note = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'ajout")

    def __unicode__(self):
        return self.category.title + " " + self.name


class WhiskyType(models.Model):
    type = models.CharField(max_length=128)

    def __unicode__(self):
        return self.type


class CoffeeCountry(models.Model):
    country = models.CharField(max_length=128)

    def __unicode__(self):
        return self.country


class Whisky(Tasting):
    old = models.IntegerField()
    type = models.ForeignKey('WhiskyType', on_delete=models.CASCADE)
    degAlcool = models.IntegerField()

    def __str__(self):
        return self.type.type + " " + self.name + " " + str(self.old) + " ans"


class Coffee(Tasting):
    country = models.ForeignKey('CoffeeCountry', on_delete=models.CASCADE)
    altitude = models.IntegerField()
    strength = models.IntegerField()

    def __str__(self):
        return self.category.title + " " + self.country.country + " " + self.name


class Wine(Tasting):
    year = models.IntegerField()
    degAlcool = models.IntegerField()

    def __str__(self):
        return self.category.title + " " + self.name