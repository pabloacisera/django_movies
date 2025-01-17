from django.shortcuts import render
from .models import Movies

def homeMovies(request):
    search_term = request.GET.get('search-text', '')

    if search_term:
        movies_search = Movies.objects.filter(title__icontains=search_term)
    else:
        movies_search = Movies.objects.all()

    return render(request, 'homeMovies.html', {'movies': movies_search, 'search_term': search_term})
