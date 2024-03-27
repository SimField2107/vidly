from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


# Create your views here.
# the Object that is passed to this function is a HTTP requests object
# first view that we map to a url
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def detail(requests, movie_id):
    return HttpResponse(movie_id)
