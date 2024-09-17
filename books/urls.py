# books/urls.py

from django.urls import path
from books.views import BookListCreateView, AuthorListCreateView, PublisherListCreateView, book_list, add_book

urlpatterns = [
    path('add/', add_book, name='add_book'),
    path('', book_list, name='book_list'),
    path('api/books/', BookListCreateView.as_view(), name='book_list_create'),
    path('api/authors/', AuthorListCreateView.as_view(), name='author_list_create'),
    path('api/publishers/', PublisherListCreateView.as_view(), name='publisher_list_create'),
]
