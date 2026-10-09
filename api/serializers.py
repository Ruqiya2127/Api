from rest_framework import serializers
from .views import Books, Genre, Comment

class BG(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'title']

        
class BooksSerializerForGenre(serializers.ModelSerializer):
    genre = BG()
    class Meta:
        model = Books
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    books =serializers.StringRelatedField(many=True)
    class Meta:
        model = Genre
        fields = ['id', 'title', 'books' ]

class GenreSerializerForDetail(serializers.ModelSerializer):
    books = BooksSerializerForGenre(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['id', 'title', 'books' ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'