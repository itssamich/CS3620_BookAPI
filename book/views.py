from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer

class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(bookCategory__icontains = 'Fantasy')
    serializer_class = BookSerializer

class AdventureViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(bookCategory__icontains = 'Adventure')
    serializer_class = BookSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(bookCategory__icontains = 'Action')
    serializer_class = BookSerializer

class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(bookCategory__icontains = 'Romance')
    serializer_class = BookSerializer

class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(bookCategory__icontains = 'Mystery')
    serializer_class = BookSerializer

class HorrorViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(bookCategory__icontains = 'Horror')
    serializer_class = BookSerializer

class MangaViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(bookCategory__icontains = 'Manga')
    serializer_class = BookSerializer

class ComicViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(bookCategory__icontains = 'Comic')
    serializer_class = BookSerializer

class SciFiViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(bookCategory__icontains = 'Sci-Fi')
    serializer_class = BookSerializer

class ThrillerViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(bookCategory__icontains = 'Thriller')
    serializer_class = BookSerializer