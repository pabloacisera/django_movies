
from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

def homeMovies(request):
    
    search_term = request.GET.get('search-text', '')

    if search_term:
        movies_search = Movies.objects.filter(title__icontains=search_term)
    else:
        movies_search = Movies.objects.all()

    return render(request, 'homeMovies.html', {'movies': movies_search, 'search_term': search_term})


def configMovies(request):
    
    films_list = Movies.objects.all()
    
    paginator = Paginator(films_list, 2) #cantidad de registros por pagina
    
    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'configMovies.html', {'page_obj': page_obj})