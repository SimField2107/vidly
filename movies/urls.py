from django.urls import path
from .import views

# define path object that maps url endpoints to view functions
# this is the URL configuartion

urlpatterns = [
    # empty string represents the root of the app
    path('', views.index, name='movies_index'),
    path('<int:movie_id>', views.detail, name='movies_detail')
]
