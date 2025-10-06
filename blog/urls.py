from django.urls import path
from . import views

urlpatterns = [
  path('', views.post_list, name='post_list'),
  path('<int:pk>/', views.post_detail, name='post_detail'),
  path('new/', views.post_create, name='post_create'),
  path('<int:pk>/edit', views.post_update, name='post_update'),
  path("delete/<int:pk>/", views.post_delete, name="post_delete"),


  # CRUD для категорий
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('categories/create/', views.category_create, name='category_create'),
]