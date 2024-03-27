from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie


# Create your views here.
# the Object that is passed to this function is a HTTP requests object
# first view that we map to a url
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def detail(requests, movie_id):

    movie = get_object_or_404(Movie, pk=movie_id)
    return render(requests, 'movies/detail.html', {'movie': movie})
