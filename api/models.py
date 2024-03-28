from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie


# Create your models/resources here. Representational State Transfer
# To represent the concept of the movie in RESTful APIs


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        excludes = ['date_created']
