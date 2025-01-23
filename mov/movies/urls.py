from django.urls import path
from .views import homeMovies,configMovies, createFilm

urlpatterns = [
	path('', homeMovies, name='homeMovies'),
	path('config', configMovies, name='configMovies'),
	path('newFilm', createFilm, name='createFilm'),
]
