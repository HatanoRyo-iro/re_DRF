from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['created_at']
        

class BookListSerializer(serializers.ListSerializer):
    """複数の本モデルを扱うためのシリアライザ"""
    
    # 対象のシリアライザを指定
    child = BookSerializer()