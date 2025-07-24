from rest_framework import serializers
from .models import Book

# Convert Book model to or from JSON and validate the input
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # Expose all the fields in the API
        fields =[
            'title', 
            'author', 
            'isbn', 
            'published_date',
            'status',
            'created_at',
            'updated_at'
        ]
        # Read-only for these fields, so users can't modify
        read_only_fields = ['created_at, updated_at']