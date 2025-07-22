from django.urls import re_path
from .views import BookView, BookDetailView

app_name = 'api'

urlpatterns = [
    # BookView.as_view() handles /books/ - create and list
    # BookDetailView.as_view() handles /books/1/ - get, put, delete
    re_path(r"^books/$", BookView.as_view(), name='book-list-create'),
    re_path(r"^books/(?P<pk>\d+)/$", BookDetailView.as_view(), name='book-detail'),
]
