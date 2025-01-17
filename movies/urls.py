from django.urls import path
from .views import homeMovies

urlpatterns = [
	path('', homeMovies, name='homeMovies'),
]
