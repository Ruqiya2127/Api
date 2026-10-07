from django.urls import path
from .views import BooksListAPIView,  RetrieveAPIView
urlpatterns =[
    path('books/', BooksListAPIView.as_view()),
    path('books/genre/<int:course_id>', BooksListAPIView.as_view()),
    path('books/<int:book_id>/', RetrieveAPIView.as_view()),
]