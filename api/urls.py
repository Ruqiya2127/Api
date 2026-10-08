from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import BookViewSet, GenreAPIView, CommentAPIView

router = SimpleRouter

router.register('books', BookViewSet)
router.register('genres', GenreAPIView)
router.register('comments', CommentAPIView)


urlpatterns = router.urls






# urlpatterns =[
#     path('books/', BookViewSet.as_view()),
#     # path('books/genre/<int:course_id>', BooksListAPIView.as_view()),
#     path('books/<int:book_id>/', BookViewSet.as_view()),
# ]