from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework import status
from .models import Genre, Books
from .serializers import BooksSerializer


class BooksListAPIView(ListCreateAPIView):
    # queryset =  Books.objects.all()
    # serializer_class = BooksSerializer

    def get_queryset(self):
        genre_id = self.kwargs.get("genre_id")
        if genre_id:
            books = Books.objects.filter(genre_id = genre_id)
        else:
            books = Books.objects.all()
        return books
    def get_serializer_class(self):
        # if self.request.user.is_staff:
        #     return BooksSerializerForAdmin
        return BooksSerializer



    
class BooksRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset =  Books.objects.all()
    serializer_class = BooksSerializer
    lookup_field = "pk"
    lookup_url_kwarg = "book_id"

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
    def get(self, request:Request, pk: int = None):
        if pk is None:
            books =  Books.objects.all()
            serializer = BooksSerializers(books, many = True)
            return Response(serializer.data)
        else:
            book= get_object_or_404(Books, pk = pk )
            return Response(BooksSerializers(book).data)

    def  post(self, request, pk: int = None):
        if pk :
            return Response({'message':"Method post not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        serializer = BooksSerializers(data= request.data)
        serializer.is_valid(raise_exception=True)

        book =serializer.save()
        return Response(BooksSerializers(book).data, status=status.HTTP_201_CREATED)
    
class GenreAPIView(APIView):
    def get(self, request:Request):
        gernes = Genre.objects.all()
        gernes_list = []

        for gerne in gernes:
            gernes_list.append(
                {
                    "id": gerne.id,
                    "title": gerne.title
                }
            )
        return Response(gernes_list)
