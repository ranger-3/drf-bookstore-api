from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.books.views import BookViewSet

router = DefaultRouter()
router.register(r"books", BookViewSet, basename="books")

urlpatterns = [
    path("", include(router.urls)),
]
