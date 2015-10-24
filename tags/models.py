from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=64)

    def __unicode__(self):
        return u"%s" % self.tag
