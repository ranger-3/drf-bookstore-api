from rest_framework.viewsets import ModelViewSet

from apps.authors.models import Author
from apps.authors.serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
