#-*- coding: utf-8 -*-
from django import forms
from recipe.models import Recipe
import floppyforms as forms


def get_categories():
    return ('1', 'Option 1'), ('2', 'Option 2')


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 5}),
        }
