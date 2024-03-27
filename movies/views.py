from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# the Object that is passed to this function is a HTTP requests object
# first view that we map to a url
def index(request):
    return HttpResponse("Hello World")
