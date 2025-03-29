from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, RecipeIngredient, RecipeImage, Ingredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']

RecipeIngredientFormset = inlineformset_factory(
    Recipe,
    RecipeIngredient,
    fields=('Quantity', 'ingredient'),
    extra=10,             # Number of empty ingredient forms you want to display by default
    can_delete=False      # Allows users to remove any extra ingredient forms
)

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']