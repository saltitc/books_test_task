from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter


class BookListView(generics.ListAPIView):
    """
    With a POST request, returns a list of all books
    Filtering can be applied by the author and year_published fields
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filter = BookFilter


class BookCreateView(generics.CreateAPIView):
    """
    With a POST request, creates a book in the database
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    With a GET request,returns detail information about the book;
    With a PUT request, updates book information;
    With a DELETE request, deletes a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
