from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Book
from datetime import date
from django.urls import reverse

class BookViewTest(APITestCase):
    # TEST 1: List books
    def test_list_books(self):
        # Create a test book in the temporary test db
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            isbn="1234567890123",
            published_date=date(2025, 1, 1),
            status="available"
        )
        # Send a GET request to /api/books/ endpoint
        url = reverse('api:books')
        response = self.client.get(url, format='json')
        # Assert response status 200 OK, returned book matches the created ones
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        returned_book = body[0]

        # Check required fields
        assert returned_book == {
            "title": book.title,
            "author": book.author,
            "isbn": book.isbn,
            "published_date": str(book.published_date),
            "status": book.status,
            "created_at": returned_book["created_at"],
            "updated_at": returned_book["updated_at"]
        }

    # TEST 2: Create a book 
    def test_create_book(self):
        data = {
            "title": "Created Book",
            "author": "Created Author",
            "isbn": "1234567890123",
            "published_date": "2025-01-01",
            "status": "available"
        }
        url = reverse('api:books')
        response = self.client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        body = response.json()
        returned_book = body

        # Check all submitted fields
        for field in data:
            assert returned_book[field] == data[field]

        # Check automanaged fields
        assert "created_at" in returned_book
        assert "updated_at" in returned_book

    # TEST 3: Retrieve a single book by ID
    def test_retrieve_book_by_id(self):
        book = Book.objects.create(
            title="Retrieved Book",
            author="Retrieved Author",
            isbn="1234567890123",
            published_date=date(2025, 1, 1),
            status="available"
        )

        url = reverse('api:book-detail', args=[book.id])
        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        returned_book = body

        assert returned_book == {
            "title": book.title,
            "author": book.author,
            "isbn": book.isbn,
            "published_date": str(book.published_date),
            "status": book.status,
            "created_at": returned_book["created_at"],
            "updated_at": returned_book["updated_at"]
        }