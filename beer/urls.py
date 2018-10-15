from django.urls import path

from . import views

urlpatterns = [
    path('', views.beer_list, name='beer_list'),
    path('add/', views.beer_create, name='beer_create'),
    path('<slug:slug>/', views.beer_details, name='beer_details'),
]
