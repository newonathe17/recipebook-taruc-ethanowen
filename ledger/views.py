from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipeList.html', {'recipes': recipes})

@login_required
def recipe_detail(request, pk):
    recipes = Recipe.objects.filter(pk=pk)
    if recipes.exists():
        recipe = recipes.first()
    else:
        return render(request, 'recipeList.html', {'recipes': Recipe.objects.all(), 'error': 'Recipe not found.'})
    return render(request, 'recipe.html', {'recipe': recipe})
