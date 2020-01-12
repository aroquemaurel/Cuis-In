from django.contrib import admin
from cuisin.recipe.models import Category, Recipe, Ingredient


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category', 'tags', 'note', 'hard')
    search_fields = 'title', 'content'

    fieldsets = (
        # Fieldset 1 : meta-info
       ('Général', {
            'classes': ['collapse',],
            'fields': ('title', 'note', 'hard', 'serves', 'preparationTime', 'cuissonTime', 'category', 'tags')
        }),

        # Fieldset 2 : contenu de la recette
        ('Contenu de l\'article', {
#           'description': '',
           'fields': ('preparation', 'ingredients')
        }),
    )


admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
