from rest_framework.test import APITestCase
from .models import Books, Comment, Genre
from .serializers import BooksSerializer, GenreSerializer, CommentSerializer
from django.urls import reverse
from django.contrib.auth.models import User


class  BookTestCase(APITestCase):
    def setUp(self):

        self.user1 = User.objects.create(user_name='Toxir')

        self.genre1 = Genre.objects.create(title= "O'zbek adabiyoti")
        self.genre1 = Genre.objects.create(title= "Jahon adabiyoti")


        self.book1 = Books.objects.create(name ="Kecha va kunduz", price = "40 000", genre_id = 1)
        self.book2 = Books.objects.create(name ="Farg'onada tong otkuncha", price = "59 000", genre_id = 1)
        self.book3 = Books.objects.create(name ="Negir bolasi", price = "40 000", genre_id = 3)

    def test_get(self):
        url = reverse('book-list')

        self.client.force_login(self.user1)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        serializer= BooksSerializer([self.book1, self.book2, self.book3], many=True)
        self.assertEqual(response.data, serializer.data)

    def test_get_search(self):
        url = reverse('book-list')

        self.client.force_login(self.user1)
        response = self.client.get(url, data={'search': '40 000'})

        self.assertEqual(response.status_code, 200)
        serializer= BooksSerializer([self.book1, self.book3], many=True)
        self.assertEqual(response.data, serializer.data)


    def test_get_filter(self):
          url = reverse('book-list')
  
          self.client.force_login(self.user1)
          response = self.client.get(url, data={'genre_title': 'Jahon adabiyoti'})
  
          self.assertEqual(response.status_code, 200)
          serializer= BooksSerializer([self.book3, self.book3], many=True)
          self.assertEqual(response.data, serializer.data)
    