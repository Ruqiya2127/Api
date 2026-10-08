from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView

from rest_framework import permissions
from rest_framework import status
from .models import Genre, Books, Comment
from .serializers import BooksSerializer, GenreSerializer, CommentSerializer
from .permissions import IsAdminOrReadOnly

from rest_framework.viewsets import ModelViewSet


class BookViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


# class BookListAPIView(GenericAPIView,
#                       mixins.ListModelMixin,
#                       mixins.CreateModelMixin,
#                       mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin):
#     queryset =Books.objects.all()
#     serializer_class = BooksSerializer
#     lookup_url_kwarg = "book_id"
#     lookup_field = "pk"

#     def get(self, request, *args, **kwargs):
#         if self.kwargs.get("book_id"):
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

    
# class BooksListAPIView(ListCreateAPIView):
#     queryset =  Books.objects.all()
#     serializer_class = BooksSerializer
#     permission_classes =[IsAdminOrReadOnly]

#     def get_queryset(self):
#         genre_id = self.kwargs.get("genre_id")
#         if genre_id:
#             books = Books.objects.filter(genre_id = genre_id)
#         else:
#             books = Books.objects.all()
#         return books
#     def get_serializer_class(self):
#         # if self.request.user.is_staff:
#         #     return BooksSerializerForAdmin
#         return BooksSerializer



    
# class BooksRetrieveAPIView(RetrieveUpdateDestroyAPIView):
#     queryset =  Books.objects.all()
#     serializer_class = BooksSerializer
#     lookup_url_kwarg = "book_id"
#     permission_classes =[IsAdminOrReadOnly]

# class BooksCreateAPIView(CreateAPIView):
#     queryset =  Books.objects.all()
#     serializer_class = BooksSerializers

# class BooksUpdateAPIView(UpdateAPIView):
#     queryset =  Books.objects.all()
#     serializer_class = BooksSerializers

# class BooksDestroyAPIView(DestroyAPIView):
#     queryset =  Books.objects.all()
#     serializer_class = BooksSerializers

# class BookAPIView(APIView):
#     def get(self, request:Request, pk: int = None):
#         if pk is None:
#             books =  Books.objects.all()
#             serializer = BooksSerializers(books, many = True)
#             return Response(serializer.data)
#         else:
#             book= get_object_or_404(Books, pk = pk )
#             return Response(BooksSerializer(book).data)

#     def  post(self, request, pk: int = None):
#         if pk :
#             return Response({'message':"Method post not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         serializer = BooksSerializer(data= request.data)
#         serializer.is_valid(raise_exception=True)

#         book =serializer.save()
#         return Response(BooksSerializer(book).data, status=status.HTTP_201_CREATED)
    
class GenreAPIView(ModelViewSet):
    queryset =  Genre.objects.all()
    serializer_class = GenreSerializer
    # def get(self, request:Request):
    #     gernes = Genre.objects.all()
    #     gernes_list = []

    #     for gerne in gernes:
    #         gernes_list.append(
    #             {
    #                 "id": gerne.id,
    #                 "title": gerne.title
    #             }
    #         )
    #     return Response(gernes_list)
class CommentAPIView(ModelViewSet):
    queryset =  Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes =[permissions.DjangoModelPermissions, IsAdminOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
