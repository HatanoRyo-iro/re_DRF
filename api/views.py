from django_filters import rest_framework as filters, generics
from rest_framework import status, views, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# class BookListCreateAPIView(views.APIView):
#     def get(self, request, *args, **kwargs):
#         book_list = Book.objects.all()
#         serializer = BookSerializer(instance=book_list, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request, *args, **kwargs):
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class BookRetrieveUpdateDestroyAPIView(views.APIView):
#     def get(self, request, pk, *args, **kwargs):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(instance=book)
#         return Response(serializer.data)
    
#     def put(self, request, pk, *args, **kwargs):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(instance=book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def patch(self, request, pk, *args, **kwargs):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(instance=book, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self, request, pk, *args, **kwargs):
#         book = get_object_or_404(Book, pk=pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)