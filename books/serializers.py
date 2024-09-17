from rest_framework import serializers
from books.models import Book, Author, Publisher

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = '__all__'
