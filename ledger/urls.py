from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('recipes/list/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe'),
]