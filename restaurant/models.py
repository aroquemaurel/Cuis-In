from django.db import models


class Restaurant(models.Model):
    title = models.CharField(max_length=128)
    note = models.IntegerField(max_length=2)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'ajout")
    reservation = models.BooleanField(default=False)
    description = models.TextField()

    def __unicode__(self):
        return u"%s" % self.title

