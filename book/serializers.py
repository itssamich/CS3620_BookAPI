from rest_framework import serializers
from .models import BookData

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookData
        fields = ['id', 'bookTitle', 'bookAuthor', 'bookCategory', 'bookRating', 'bookDescription', 'bookImage']