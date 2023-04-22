from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('../', views.index),
    path('about/', views.about),
    path('reviews/', views.reviews, name='reviews'),
    path('reviewlist/', views.reviewlist),
    path('services/', views.services),
]