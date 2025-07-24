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
        returned_book = response.json()

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
        returned_book = response.json()

        assert returned_book == {
            "title": book.title,
            "author": book.author,
            "isbn": book.isbn,
            "published_date": str(book.published_date),
            "status": book.status,
            "created_at": returned_book["created_at"],
            "updated_at": returned_book["updated_at"]
        }

    # TEST 4: Update a book by ID
    def test_update_book(self):
        # Create an original book
        book = Book.objects.create(
            title="Original Book",
            author="Original Author",
            isbn="1234567890123",
            published_date=date(2025, 1, 1),
            status="available"
        )

        # Prepare the updated data
        updated_data= {
            "title": "Updated Book",
            "author":"Updated Author",
            "isbn": "1234567890123",
            "published_date": "2025-01-01",
            "status": "checked_out"
        }

        # Send PUT request to the detail endpoint
        url = reverse('api:book-detail', args=[book.id])
        response = self.client.put(url, updated_data, format='json')

        # Assert correct response and values updated
        assert response.status_code == status.HTTP_200_OK
        returned_book = response.json()

        for key in updated_data:
            assert returned_book[key] == updated_data[key]
        
    # TEST 5: Delete a book by ID
    def test_delete_book(self):
        # Create a book to delete
        book = Book.objects.create(
            title="Delete Book",
            author="Delete Author",
            isbn="1234567890123",
            published_date=date(2025, 1, 1),
            status="available"
        )

        # Send DELETE request to the detail endpoint
        url = reverse('api:book-detail', args=[book.id])
        response = self.client.delete(url)

        # Assert response is 204 no content
        assert response.status_code == status.HTTP_204_NO_CONTENT

        # Confirm book no longer exists
        exists = Book.objects.filter(id=book.id).exists()
        assert exists is False
    
    # TEST 6: Creating a book with invalid data to check the serializer logic
    def test_create_book_with_invalid_data(self):
        # Missing title and isbn is too short - invalid
        invalid_data = {
            "author": "Invalid Author",
            "isbn": "123",
            "published_date": "2025-01-01",
            "status": "available"
        }

        url = reverse('api:books')
        response = self.client.post(url, invalid_data, format='json')

        # Assert 400 bad request
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        # Check error fields returned
        returned_book = response.json()
        assert "title" in returned_book
        assert "isbn" in returned_book