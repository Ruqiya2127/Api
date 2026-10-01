from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework import status
from .models import Genre, Books
from django.forms import model_to_dict
class BookAPIView(APIView):
    def get(self, request:Request):
        books =  Books.objects.all()
        books_list = []

        for book in books:
            books_list.append(
                {
                    "id": books.id,
                    "name": books.name,
                    "description": books.description,
                    "price": books.price,
                    "created": books.created,
                    "updated": books.updated,
                    "published": books.published,
                    "genre_id": books.genre.id
                }
            )
        return Response(books_list)
    
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

def  post(self, request):
    book = Books.objects.create(**request.data)
    book_dict = model_to_dict(book)
    del book_dict["image"]
    return Response(book_dict, status=status.HTTP_201_CREATED)