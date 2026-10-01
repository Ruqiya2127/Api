from django.urls import path
from .views import BookAPIView, GenreAPIView

urlpatterns =[
    path('books/', BookAPIView.as_view()),
    path('gerne/', GenreAPIView.as_view())
]