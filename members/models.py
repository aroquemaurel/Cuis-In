from django.contrib.auth.models import User
from django.db import models

class UserInfo(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")

    def __unicode__(self):
        return u"Profil de {0}".format(self.user.username)