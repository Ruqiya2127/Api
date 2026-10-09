

from rest_framework import permissions

from .models import Genre, Books, Comment
from .serializers import BooksSerializer, GenreSerializer, CommentSerializer, GenreSerializerForDetail
from .permissions import IsAdminOrReadOnly

from rest_framework.viewsets import ModelViewSet


class BookViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

    
class GenreAPIView(ModelViewSet):
    queryset =  Genre.objects.all()
    serializer_class = GenreSerializer
    def get_serializer_class(self):
        if self.kwargs.get('pk'):
            return GenreSerializerForDetail
        return GenreSerializer

class CommentAPIView(ModelViewSet):
    queryset =  Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes =[permissions.DjangoModelPermissions, IsAdminOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
