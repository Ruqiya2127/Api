from rest_framework import serializers
from .views import Books, Genre, Comment

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        # fields = '__all__'
        # fields = ['name', 'describtion', 'image', 'price' ]
        exclude = ['image']
        depth = 1
        read_only_fields = ['desciription']

# class BooksSerializerForAdmin(serializers.ModelSerializer):
#     class Meta:
#         model = Books
#         fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# class BooksSerializers(serializers.Serializer):
#     id = serializers.BigIntegerField(read_only = True)
#     name = serializers.CharField(max_length=250, required=True)
#     description = serializers.CharField(max_length=255)
#     image = serializers.ImageField(required = False)
#     price = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
#     created = serializers.DateTimeField()
#     updated = serializers.DateTimeField()
#     published = serializers.BooleanField()
#     genge_id  = serializers.IntegerField()

#     def create(self, validated_data):
#         return Books.objects.create(**validated_data)