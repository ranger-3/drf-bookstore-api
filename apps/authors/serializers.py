from rest_framework import serializers

from apps.authors.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "first_name",
            "last_name",
            "birth_date",
            "death_date",
        )
