from apps.authors.models import Author
from apps.authors.serializers import AuthorSerializer
from apps.common.views import BaseViewSet


class AuthorViewSet(BaseViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
