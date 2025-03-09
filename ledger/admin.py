from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('name',)

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('name',)
    inlines = [RecipeIngredientInline,]

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'Quantity', 'ingredient', 'recipe',)
    search_fields = ('Quantity',)
    list_filter = ('recipe', 'ingredient',)

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
