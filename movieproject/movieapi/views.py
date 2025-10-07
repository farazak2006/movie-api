from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

from django.shortcuts import render
from .models import Movie   # Correct import

def home(request):
    movies = Movie.objects.all()
    return render(request, 'movieapi/home.html', {'movies': movies})
