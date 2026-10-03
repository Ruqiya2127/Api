from rest_framework import serializers
from .views import Books

class BooksSerializers(serializers.Serializer):
    id = serializers.BigIntegerField(read_only = True)
    name = serializers.CharField(max_length=250, required=True)
    description = serializers.CharField(max_length=255)
    image = serializers.ImageField(required = False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    published = serializers.BooleanField()
    genge_id  = serializers.IntegerField()

    def create(self, validated_data):
        return Books.objects.create(**validated_data)