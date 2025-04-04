from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class ProfileinLine(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileinLine,]

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('name',)

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'created_on', 'updated_on',)
    search_fields = ('name',)
    list_filter = ('name', 'author', 'created_on', 'updated_on',)
    inlines = [RecipeIngredientInline,]

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'Quantity', 'ingredient', 'recipe',)
    search_fields = ('Quantity',)
    list_filter = ('recipe', 'ingredient',)

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
