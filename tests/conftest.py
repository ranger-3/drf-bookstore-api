import pytest
from django.contrib.auth import get_user_model
from model_bakery import baker
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def user():
    return baker.make(get_user_model())


@pytest.fixture
def author():
    return baker.make("authors.Author")


@pytest.fixture
def book(author):
    return baker.make("books.Book", author=author)
