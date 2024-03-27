from django.urls import path
from .import views

# define path object that maps url endpoints to view functions
# this is the URL configuartion


app_name = 'movies'
urlpatterns = [
    # empty string represents the root of the app
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]
