from rest_framework.viewsets import ModelViewSet

from apps.books.models import Book
from apps.books.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
