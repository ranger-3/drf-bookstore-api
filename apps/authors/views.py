from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.authors.models import Author
from apps.authors.serializers import AuthorSerializer
from apps.books.models import Book
from apps.books.serializers import BookSerializer
from apps.common.views import BaseViewSet


class AuthorViewSet(BaseViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @extend_schema(responses=BookSerializer(many=True))
    @action(detail=True, methods=["get"])
    def books(self, request, pk=None):
        author = self.get_object()
        queryset = Book.objects.filter(author=author)
        serializer = BookSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    @extend_schema(request=BookSerializer, responses={201: BookSerializer})
    @books.mapping.post
    def create_book(self, request, pk=None):
        author = self.get_object()
        serializer = BookSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        book = serializer.save(author=author)
        return Response(
            BookSerializer(book, context={"request": request}).data,
            status=status.HTTP_201_CREATED,
        )
