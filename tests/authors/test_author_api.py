import pytest
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_authors_list_empty(api_client):
    url = reverse("author-list")
    response = api_client.get(url)
    assert (response.status_code, response.json()) == (status.HTTP_200_OK, [])


def test_authors_create(api_client):
    url = reverse("author-list")
    expected = {
        "first_name": "Erich",
        "last_name": "Remarque",
        "birth_date": "1898-06-22",
        "death_date": "1970-09-25",
    }
    response = api_client.post(url, expected, format="json")
    actual = response.json()

    assert (
        response.status_code,
        actual["first_name"],
        actual["last_name"],
    ) == (
        status.HTTP_201_CREATED,
        expected["first_name"],
        expected["last_name"],
    )


def test_authors_retrieve(api_client, author):
    url = reverse("author-detail", args=[author.id])
    response = api_client.get(url)
    actual = response.json()

    assert (
        response.status_code,
        actual["first_name"],
        actual["last_name"],
    ) == (
        status.HTTP_200_OK,
        author.first_name,
        author.last_name,
    )


def test_authors_partial_update(api_client, author):
    url = reverse("author-detail", args=[author.id])
    response = api_client.patch(url, {"first_name": "Updated"}, format="json")
    actual = response.json()

    assert (
        response.status_code,
        actual["first_name"],
    ) == (
        status.HTTP_200_OK,
        "Updated",
    )


def test_authors_delete(api_client, author):
    url = reverse("author-detail", args=[author.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT

    response2 = api_client.get(url)
    assert response2.status_code == status.HTTP_404_NOT_FOUND
