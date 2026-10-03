from django.urls import path
from .views import BooksListAPIView, BooksRetrieveAPIView

urlpatterns =[
    path('books/', BooksListAPIView.as_view()),
    path('books/genre/<int:course_id>', BooksListAPIView.as_view()),
    # path('books/create/', BooksCreateAPIView.as_view()),
    path('books/<int:book_id>/', BooksRetrieveAPIView.as_view()),
    # path('books/<int:pk>/update/', BooksUpdateAPIView.as_view()),
    # path('books/<int:pk>/delete/', BooksDestroyAPIView.as_view()),


]