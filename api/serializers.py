from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['created_at']
        validator = [
            # タイトルと価格でユニークになっていることを検証
            UniqueTogetherValidator(
                queryset=Book.objects.all(),
                fields=('title', 'price'),
                message="タイトルと価格でユニークになっていなければいけません。"
            ),
        ],
        extra_kwargs = {
            'title': {
                'validators': [
                    RegexValidator(
                        r'^D.+$', message="タイトルはDで始まる必要があります。"
                    ),
                ],
            },
        }
        
        
def validate_title(self, value):
    if "Java" in value:
        raise serializers.ValidationError("Javaは含めません。")
    return value

def validate(self, data):
    title = data.get('title')
    price = data.get('price')
    if title and '薄い本' in title and price and price > 3000:
        raise serializers.ValidationError("薄い本は3000円を超えてはいけません。")
    return data


class BookListSerializer(serializers.ListSerializer):
    """複数の本モデルを扱うためのシリアライザ"""
    
    # 対象のシリアライザを指定
    child = BookSerializer()