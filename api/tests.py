import json
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Books, Comment, Genre
from .serializers import BooksSerializer, GenreSerializer, CommentSerializer


class  BookTestCase(APITestCase):
    def setUp(self):

        self.user1 = User.objects.create_user(user_name="admin", password="admin")

        login_url = reverse('token_obtain_pair')
        response = self.client.post(login_url, data={"username":"admin", "password":"admin"})
        self.assertEqual(response.status_code, 200)
        access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION= "Bearer" + access_token)

        self.genre1 = Genre.objects.create(title= "O'zbek adabiyoti")
        self.genre1 = Genre.objects.create(title= "Jahon adabiyoti")

        image = SimpleUploadedFile(name="test.jpg", content=b"fake image content", content_type="image/jpeg")

        self.book1 = Books.objects.create(name ="Kecha va kunduz", price = "40 000", genre_id = 1, image=image)
        self.book2 = Books.objects.create(name ="Farg'onada tong otkuncha", price = "59 000", genre_id = 1,image=image)
        self.book3 = Books.objects.create(name ="Negir bolasi", price = "40 000", genre_id = 3, image=image)

    def test_get(self):
        url = reverse('book-list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        serializer= BooksSerializer([self.book1, self.book2, self.book3], 
            many=True,
            context={'request': response.wsi_request}
        )
        self.assertEqual(response.data, serializer.data)

    def test_get_search(self):
        url = reverse('book-list')

        
        response = self.client.get(url, data={'search': '40 000'})

        self.assertEqual(response.status_code, 200)
        serializer= BooksSerializer([self.book1, self.book3], many=True, context={'request': response.wsi_request})
        self.assertEqual(response.data, serializer.data)

    def test_get_ordering(self):
        url = reverse('book-list')

        
        response = self.client.get(url, data={'ordering': 'name'})

        self.assertEqual(response.status_code, 200)
        serializer= BooksSerializer([self.book3, self.book2, self.book1], many=True, context={'request': response.wsi_request})
        self.assertEqual(response.data, serializer.data)

    def test_get_filter(self):
          url = reverse('book-list')
  
          response = self.client.get(url, data={'genre_title': 'Jahon adabiyoti'})
  
          self.assertEqual(response.status_code, 200)
          serializer= BooksSerializer([self.book3, self.book3], many=True, context={'request': response.wsi_request})
          self.assertEqual(response.data, serializer.data)

    def test_create(self):
        url = reverse('book-list')
        data =  {
            "name": "Kecha va kunduz",
            'price': "30 000",
            'genre': "2"
        }
        json_data= json.dumps(data)
        response = self.client.post(url, data=json_data, content_type="application/json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Books.objects.all().count(), 4)

    def test_update(self):
        url = reverse('book-detail', args=(self.book1.pk,))
        data =  {
            "name": self.book1.name,
            'price': "50 000",
            'genre': self.book1.genre.pk
        }
        json_data= json.dumps(data)
        response = self.client.put(url, data=json_data, content_type="application/json")

        self.assertEqual(response.status_code, 200)
        self.book1.refresh_from_db()
        self.assertEqual(response.data.get('price'), self.book1.price)

    def test_pertial_update(self):
        url = reverse('book-detail', args=(self.book1.pk,))
        data =  {
            'price': "50 000",
        }
        json_data= json.dumps(data)
        response = self.client.pacht(url, data=json_data, content_type="application/json")

        self.assertEqual(response.status_code, 200)
        self.book1.refresh_from_db()
        self.assertEqual(response.data.get('price'), self.book1.price)


    def test_delete(self):
        url = reverse('book-detail', args=(self.book3.pk,))

        self.client.force_login(self.user1)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Books.objects.all().count(), 2)

  
   

