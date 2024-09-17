# books/urls.py

from django.urls import path
from books.views import BookListView, BookDetailView, AuthorDetailView, PublisherDetailView, book_list, add_book

urlpatterns = [
    path('add/', add_book, name='add_book'),
    path('', book_list, name='book_list'),
    path('api/books/', BookListView.as_view(), name='book_list'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('api/authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('api/publishers/<int:pk>/', PublisherDetailView.as_view(), name='publisher_detail'),
]
