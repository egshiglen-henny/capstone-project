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
            author="Author Name",
            isbn="1234567890000",
            published_date=date(2025, 1, 1)
        )
        # Send a GET request to /api/books/ endpoint
        url = reverse('api:books')
        response = self.client.get(url, format='json')
        # Assert response status 200 OK, returned book matches the created ones
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        returned_book = body[0]
        assert returned_book == {
            "title": book.title,
            "author": book.author,
            "isbn": book.isbn,
            "published_date": str(book.published_date)
        }

    # TEST 2: Create a book 
    def test_create_book(self):
        data = {
            "title": "Created Book",
            "author": "Created Author",
            "isbn": "1234567890123",
            "published_date": "2025-01-01"
        }
        url = reverse('api:books')
        response = self.client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        body = response.json()
        for field in data:
            assert body[field] == data[field]
        

