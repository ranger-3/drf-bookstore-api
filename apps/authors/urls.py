from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.authors.views import AuthorViewSet

router = DefaultRouter()
router.register(r"authors", AuthorViewSet, basename="authors")

urlpatterns = [
    path("", include(router.urls)),
]
