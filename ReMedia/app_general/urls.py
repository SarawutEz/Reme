from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Movies', views.Movies, name='Movies'),
    path('Movie', views.Movie, name='Movie'),
]