from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework import status
from .models import Genre, Books
from .serializers import BooksSerializers

class BookAPIView(APIView):
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
