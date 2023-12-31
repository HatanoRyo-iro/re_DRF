from rest_framework import viewsets


from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    

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