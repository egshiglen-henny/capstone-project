from django.urls import re_path
from .views import book_view, book_detail_view, health_view, test_view

app_name = 'api'

urlpatterns = [
    # BookView.as_view() handles /books/ - create and list
    re_path(r"^books/$", book_view, name='books'),
    # BookDetailView.as_view() handles /books/1/ - get, update, delete
    re_path(r"^books/(?P<pk>\d+)/$", book_detail_view, name='book-detail'),
    re_path(r"^health/$", health_view, name='health'),
    re_path(r"^test/$", test_view, name='test'),
]
