from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    price = serializers.CharField(read_only=True)
    
    class Meta:
        model = Book
        exclude = ['created_at']
        extra_kwargs = {
            'title': {
                'write_only': True,
                'max_length': 10,
            }
        }