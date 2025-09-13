from rest_framework.viewsets import ModelViewSet

from apps.books.models import Book
from apps.books.serializers import BookSerializer
from apps.common.views import BaseViewSet


class BookViewSet(BaseViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
