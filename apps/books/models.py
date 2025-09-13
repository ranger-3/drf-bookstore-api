from django.db import models

from apps.books.validators import validate_isbn
from apps.common.models import BaseModel


class Book(BaseModel):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(
        max_length=13,
        unique=True,
        null=True,
        blank=True,
        validators=[validate_isbn],
    )
    author = models.ForeignKey(
        "authors.Author",
        related_name="books",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
