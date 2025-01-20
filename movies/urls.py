from django.urls import path
from .views import homeMovies,configMovies

urlpatterns = [
	path('', homeMovies, name='homeMovies'),
	path('config', configMovies, name='configMovies'),
]
