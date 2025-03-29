from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm, RecipeIngredientForm

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'ledger/recipe_list.html', {'recipes': recipes})

@login_required
def recipe_detail(request, pk):
    recipes = Recipe.objects.filter(pk=pk)
    if recipes.exists():
        recipe = recipes.first()
    else:
        return render(request, 'ledger/recipe_list.html', {'recipes': Recipe.objects.all(), 'error': 'Recipe not found.'})
    return render(request, 'ledger/recipe_detail.html', {'recipe': recipe})

@login_required
def recipe_add_image(request, pk):
    recipes = Recipe.objects.filter(pk=pk)
    if recipes.exists():
        recipe = recipes.first()
    else:
        # Handle the case where no recipe is found; for example, redirect to the recipe list with an error.
        return redirect('recipe_list')
    
    if request.method == 'POST':
        # Process form data to create a RecipeImage instance (implementation goes here)
        # After processing, redirect to the recipe detail page.
        return redirect(recipe.get_absolute_url())
    
    return render(request, 'ledger/recipe_add_image.html', {'recipe': recipe})
@login_required
def recipe_add(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        ingredient_form = RecipeIngredientForm(request.POST)
        if recipe_form.is_valid() and ingredient_form.is_valid():
           
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            
            recipe_ingredient = ingredient_form.save(commit=False)
            recipe_ingredient.recipe = recipe
            recipe_ingredient.save()

            return redirect(recipe.get_absolute_url())
    else:
        recipe_form = RecipeForm()
        ingredient_form = RecipeIngredientForm()

    context = {
        'recipe_form': recipe_form,
        'ingredient_form': ingredient_form,
    }
    return render(request, 'ledger/recipe_add.html', context)


def homepage(request):
    return redirect('login')

