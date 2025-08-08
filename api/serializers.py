from datetime import date
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    # Serializer for converting Book model instances to and from JSON,
    # and for validating incoming API request data.

    class Meta:
        model = Book
        # Expose all the fields in the API
        fields =[
            'id',
            'title', 
            'author', 
            'isbn', 
            'published_date',
            'status',
            'created_at',
            'updated_at'
        ]
        # Read-only for these fields, so users can't modify
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_isbn(self, value):
        # Ensure ISBN is exactly 13 digits (allowing hyphens, but ignoring them in count).
        cleaned_value = value.replace("-", "").strip()
        if not cleaned_value.isdigit() or len(cleaned_value) != 13:
            raise serializers.ValidationError(
                "The ISBN must be exactly 13 numeric digits. Hyphens are optional."
            )
        return value

    def validate_published_date(self, value):
        # Ensure the published date is not set in the future.
        if value and value > date.today():
            raise serializers.ValidationError(
                "The published date cannot be set in the future."
            )
        return value

    def validate(self, data):
        # General validation for all fields.
        # Removes leading/trailing spaces from text fields.
        for field_name in ("title", "author"):
            if field_name in data and isinstance(data[field_name], str):
                data[field_name] = data[field_name].strip()
        return data
