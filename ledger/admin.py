from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Profile, RecipeImage  
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html


class ProfileinLine(admin.StackedInline):
    model = Profile
    can_delete = False
    
class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.image.url)
        return ""
    image_preview.short_description = "Image Preview"

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileinLine,]

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'created_on', 'updated_on',)
    search_fields = ('name',)
    list_filter = ('name', 'author', 'created_on', 'updated_on',)
    inlines = [RecipeIngredientInline,]

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'Quantity', 'ingredient', 'recipe',)
    search_fields = ('Quantity',)
    list_filter = ('recipe', 'ingredient',)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'created_on', 'updated_on',)
    search_fields = ('name',)
    list_filter = ('name', 'author', 'created_on', 'updated_on',)
    inlines = [RecipeIngredientInline, RecipeImageInline]

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
