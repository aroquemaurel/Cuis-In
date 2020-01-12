from django.contrib import admin
from cuisin.recipe.models import Category, Recipe


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


class CategoryAdmin(admin.ModelAdmin):
    fields = 'title',


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)

