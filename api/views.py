

from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Genre, Books, Comment
from .serializers import BooksSerializer, GenreSerializer, CommentSerializer
from rest_framework import permissions

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter


class BookViewSet(ModelViewSet):
    # queryset = Books.objects.all().prefetch_related('genre').only('id', 'name', 'price', 'genre')
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'price']
    ordering_fields = ['id', 'name', 'genre']
    filterset_fields = {
        'genre__title' : ['exact'],
        'price' : ['exact', 'lt', 'lte', 'gt', 'gte']
    }
  

    
class GenreAPIView(ModelViewSet):
    queryset =  Genre.objects.all().prefetch_related('book')
    serializer_class = GenreSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['id']
   

class CommentAPIView(ModelViewSet):
    queryset =  Comment.objects.all()
    serializer_class = CommentSerializer
