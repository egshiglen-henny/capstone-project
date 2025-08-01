from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Book

class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {"status": "ok"}
        )
health_view = HealthView.as_view()

class BookView(APIView):
    # List all books, or create a new book
    
    def get(self, request, *args, **kwargs):
        # List all books
        # Get all books in the table
        all_books = Book.objects.all()
        # Serialize the list of books
        serializer = BookSerializer(all_books, many=True)
        # Return the serialized JSON response
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Create a new book
        # Pass the request data to the serializer for validation
        serializer = BookSerializer(data = request.data)
        # If the data is valid, create and save the new book to the db
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is invalid, return 400 with validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
book_view = BookView.as_view()

class BookDetailView(APIView):
    # Retrieve, update or delete a book by ID
    # Handle a single book
    # pk = primary key
    
    def get_object(self, pk):
        # Fetch the book with the given ID
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            # If not found, raise a 404 error
            raise Http404

    def get(self, request, pk):
        # Retrieve a single book
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        # Update a book with new data
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)

        # If new data is valid, save the changes
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # If not valid, return 400 with error details
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Delete the specific book
        book = self.get_object(pk)
        book.delete()
        # Return 204 no content to confirm the deletion
        return Response(status=status.HTTP_204_NO_CONTENT)
book_detail_view = BookDetailView.as_view()