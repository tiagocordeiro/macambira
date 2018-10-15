from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.beer_create, name='beer_create'),
    path('list/', views.beer_list, name='beer_list'),
]
