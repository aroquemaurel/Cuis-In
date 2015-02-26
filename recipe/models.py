from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=128)
    # category TODO add a category for a recipe
    note = models.IntegerField(max_length=2)
    hard = models.IntegerField(max_length=2)
    serves = models.IntegerField(max_length=2)
    preparationTime = models.IntegerField(max_length=4)
    cuissonTime = models.IntegerField(max_length=4)
    preparation = models.TextField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'ajout")

    def __unicode__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que nous
        traiterons plus tard et dans l'administration
        """
    return u"%s" % self.title