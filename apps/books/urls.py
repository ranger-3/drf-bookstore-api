from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.books.views import BookViewSet

app_name = "books"

router = DefaultRouter()
router.register(r"books", BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
