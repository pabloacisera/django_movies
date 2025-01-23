
from django.shortcuts import render, redirect
from .models import Movies
from django.core.paginator import Paginator
from django.db import IntegrityError
from .forms import MovieForm


def homeMovies(request):
    
    search_term = request.GET.get('search-text', '')

    if search_term:
        movies_search = Movies.objects.filter(title__icontains=search_term).order_by('-created_at')
    else:
        movies_search = Movies.objects.all().order_by('-created_at')

    return render(request, 'homeMovies.html', {'movies': movies_search, 'search_term': search_term})


def configMovies(request):
    
    films_list = Movies.objects.all()
    
    paginator = Paginator(films_list, 10) #cantidad de registros por pagina
    
    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'configMovies.html', {'page_obj': page_obj})
    
def createFilm(request):
    if request.method == 'POST':
        
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo registro en la base de datos
            return redirect('homeMovies')  # Redirige a la página de inicio
        else:
            return render(request, 'createFilm.html', {'form': form})  # Devuelve errores en el formulario
    else:
        form = MovieForm()
        return render(request, 'createFilm.html', {'form': form})
    
