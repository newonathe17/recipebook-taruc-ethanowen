from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('recipes/list/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe'),
    path('recipe/<int:pk>/add_image/', views.recipe_add_image, name='recipe_add_image'),
    path('recipe/add/', views.recipe_add, name='recipe_add'),
    path('recipe/image/<int:image_id>/delete/', views.recipe_image_delete, name='recipe_image_delete'),
]