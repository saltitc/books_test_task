from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    With a POST request, returns a list of all books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


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
    queryset = Book.objects.get(id=1)
    serializer_class = BookSerializer
