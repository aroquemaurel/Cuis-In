from django.contrib import admin
from tasting.models import Whisky, WhiskyType, Coffee, CoffeeCountry, Wine, TastingCategory

admin.site.register(Whisky)
admin.site.register(WhiskyType)
admin.site.register(Coffee)
admin.site.register(CoffeeCountry)
admin.site.register(Wine)
admin.site.register(TastingCategory)