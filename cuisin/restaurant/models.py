from django.db import models
from cuisin.tags.models import Tag


class Restaurant(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, default="")
    note = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'ajout")
    reservation = models.BooleanField(default=False)
    description = models.TextField()

    # Contacts informations
    phone = models.CharField(max_length=16, default="")
    website = models.CharField(max_length=128, default="")
    address = models.CharField(max_length=128, default="")
    postalcode = models.CharField(max_length=16, default="")
    city = models.CharField(max_length=128, default="")

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return u"%s" % self.title

