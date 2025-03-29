from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeImage, RecipeIngredient
from .forms import RecipeForm, RecipeIngredientFormset, RecipeImageForm, IngredientForm

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
        return redirect('recipe_list')
    
    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            return redirect(recipe.get_absolute_url())
    else:
        form = RecipeImageForm()

    return render(request, 'ledger/recipe_add_image.html', {'recipe': recipe, 'form': form})
@login_required
def recipe_add(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        formset = RecipeIngredientFormset(request.POST)
        if recipe_form.is_valid() and formset.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            formset.instance = recipe
            formset.save()
            return redirect(recipe.get_absolute_url())
    else:
        recipe_form = RecipeForm()
        # Use an empty queryset to force the display of extra forms
        formset = RecipeIngredientFormset(queryset=RecipeIngredient.objects.none())
    
    context = {
        'recipe_form': recipe_form,
        'formset': formset,
    }
    return render(request, 'ledger/recipe_add.html', context)

@login_required
def recipe_image_delete(request, image_id):
    image_qs = RecipeImage.objects.filter(pk=image_id)
    if image_qs.exists():
        image = image_qs.first()
        # Retrieve the recipe using filter
        recipes = Recipe.objects.filter(pk=image.recipe.pk)
        if recipes.exists():
            recipe = recipes.first()
        else:
            return redirect('recipe_list')
        
        # Optionally enforce that only the recipe's author can delete its images
        if request.user != recipe.author:
            return redirect(recipe.get_absolute_url())
        
        image.delete()
        return redirect(recipe.get_absolute_url())
    else:
        return redirect('recipe_list')

@login_required
def ingredient_add(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_add')
    else:
        form = IngredientForm()
    return render(request, 'ledger/ingredient_add.html', {'form': form})
def homepage(request):
    return redirect('login')

