from django.db import models
from django.core.validators import RegexValidator

class Book(models.Model):
    # Title of the book (max 255 characters)
    title = models.CharField(max_length=255)
    # Author of the book (max 255 characters)
    author = models.CharField(max_length=255)
    # ISBN number (must be unique and exactly 13 digits using regex validation)
    isbn = models.CharField(
        max_length=13,
        unique=True,
        validators=[
            RegexValidator(
                r'^\d{13}$', 
                message='ISBN must be 13 digits'
            )
        ]
    )
    # Published date of the book (format: YYYY-MM-DD)
    published_date = models.DateField()
    # Status of the book: available or archived
    status = models.CharField(
        max_length=20,
        choices=[
            ('available', 'Available'), 
            ('archived', 'Archived'),
            ('checked_out', 'Checked out'),
        ],
        default='available' # Default value when creating a new book
    )
    # Timestamp when the book was first created (auto-set on creation)
    created_at = models.DateTimeField(auto_now_add=True)
    # Timestamp when the book was last updated (auto-updates on each save)
    updated_at = models.DateTimeField(auto_now=True)

    # String representation of the book (e.g. "The Hobbit by Tolkien (1937)")
    def __str__(self):
        return f"{self.title} by {self.author} ({self.published_date.year})"
    
    class Meta:
        ordering = ['title'] # Sort books alphabetically by title by default
        verbose_name = 'Book'
        verbose_name_plural = 'Books'