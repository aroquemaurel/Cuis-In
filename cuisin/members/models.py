from django.contrib.auth.models import User
from django.db import models

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=256)

    def __unicode__(self):
        return u"Profil de {0}".format(self.user.username)