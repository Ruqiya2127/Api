from rest_framework import serializers
from .views import Books, Genre, Comment

        
class BooksSerializer(serializers.ModelSerializer):
    # course_name = serializers.CharField(source = 'genre.title', read_only = True)
    class Meta:
        model = Books
        # fields = '__all__'
        exclude = ['image', 'description']


class GenreSerializer(serializers.ModelSerializer):
    # book = BooksSerializer(many=True)
    class Meta:
        model = Genre
        fields = ['id', 'title', 'books' ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'