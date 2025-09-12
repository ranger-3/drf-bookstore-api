from django.core.exceptions import ValidationError
from pydantic_core import PydanticCustomError
from pydantic_extra_types.isbn import ISBN


def validate_isbn(value: str) -> None:
    try:
        ISBN.validate_isbn_format(value)
    except PydanticCustomError as e:
        raise ValidationError(str(e)) from e
