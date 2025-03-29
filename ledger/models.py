from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.id)])

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.id)])
    
class RecipeIngredient(models.Model):
    Quantity = models.CharField(max_length=100)

    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE, 
        related_name="recipe")
    
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE, 
        related_name="ingredients")
    
    def __str__(self):
        return f"{self.Quantity} of {self.ingredient.name}"
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

class RecipeImage(models.Model):
    image = models.ImageField(upload_to='recipe_images/')
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return f"Image for {self.recipe.name}"
