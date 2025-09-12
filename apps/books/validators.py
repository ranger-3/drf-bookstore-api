from django.core.exceptions import ValidationError
from pydantic_extra_types.isbn import ISBN


def validate_isbn(value: str) -> None:
    try:
        ISBN.validate_isbn_format(value)
    except Exception as e:
        raise ValidationError("Invalid ISBN") from e
