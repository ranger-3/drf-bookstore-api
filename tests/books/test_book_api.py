import pytest
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_books_list_empty(api_client):
    url = reverse("books:book-list")
    response = api_client.get(url)
    assert (response.status_code, response.json()) == (status.HTTP_200_OK, [])


def test_books_create(api_client, author):
    url = reverse("books:book-list")
    payload = {
        "title": "Clean Architecture",
        "isbn": "9780134494166",
        "authors": author.id,
        "published_year": 2017,
    }
    response = api_client.post(url, payload, format="json")
    data = response.json()

    assert (
        response.status_code,
        data["title"],
    ) == (
        status.HTTP_201_CREATED,
        payload["title"],
    )


def test_books_retrieve(api_client, book):
    url = reverse("books:book-detail", args=[book.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_books_partial_update(api_client, book):
    url = reverse("books:book-detail", args=[book.id])
    response = api_client.patch(url, {"title": "Patch Title"}, format="json")

    assert (
        response.status_code,
        response.json()["title"],
    ) == (
        status.HTTP_200_OK,
        "Patch Title",
    )


def test_books_delete(api_client, book):
    url = reverse("books:book-detail", args=[book.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT

    response2 = api_client.get(url)
    assert response2.status_code == status.HTTP_404_NOT_FOUND
