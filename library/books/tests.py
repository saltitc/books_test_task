import json
from django.db import connection
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from .serializers import BookSerializer
from django.test.utils import CaptureQueriesContext


class BooksApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.book_1 = Book.objects.create(title='Test book 1', author='Author 1',
                                          year_published='2023-10-10', isbn='4129418247125')
        self.book_2 = Book.objects.create(title='Test book 2', author='Author 2',
                                          year_published='2023-10-11', isbn='8412491244891')
        self.book_3 = Book.objects.create(title='Test book 3', author='Author 3',
                                          year_published='2023-10-12', isbn='5012748219401')

    def test_book_list(self):
        url = reverse('api:book-list')
        with CaptureQueriesContext(connection) as queries:
            response = self.client.get(url)
            self.assertEqual(1, len(queries))
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(serializer_data[0]['title'], 'Test book 1')
        self.assertEqual(serializer_data[1]['author'], 'Author 2')
        self.assertEqual(serializer_data[2]['isbn'], '5012748219401')

    def test_filter_books_by_author(self):
        url = reverse('api:book-list')
        books = Book.objects.filter(author='Author 1')
        response = self.client.get(url, {'author': 'Author 1'})
        serializer_data = BookSerializer(books, many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(serializer_data, response.data)

    def test_filter_books_by_year_published(self):
        url = reverse('api:book-list')
        books = Book.objects.filter(year_published='2023-10-11')
        response = self.client.get(url, {'year_published': '2023-10-11'})
        serializer_data = BookSerializer(books, many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(serializer_data, response.data)

    def test_get_book_detail(self):
        url = reverse('api:book-detail', args=(self.book_2.id,))
        book_data = {
            'id': 2,
            'title': 'Test book 2',
            'author': 'Author 2',
            'year_published': '2023-10-11',
            'isbn': '8412491244891'
        }
        book = Book.objects.get(id=2)
        serializer_data = BookSerializer(book).data
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(book_data, serializer_data)
        self.assertEqual(serializer_data, response.data)

    def test_book_create(self):
        self.assertEqual(3, Book.objects.all().count())
        url = reverse('api:book-create')
        data = {
            'title': 'Test book 4',
            'author': 'Author 4',
            'year_published': '2023-10-13',
            'isbn': '5129417284121'
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Book.objects.all().count())
        self.assertEqual('5129417284121', Book.objects.last().isbn)

    def test_book_update(self):
        url = reverse('api:book-detail', args=(self.book_1.id,))
        data = {
            'title': 'Test book 1',
            'author': 'Author 1',
            'year_published': '2023-10-10',
            'isbn': '1111418241111'
        }
        json_data = json.dumps(data)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.book_1.refresh_from_db()
        self.assertEqual('1111418241111', self.book_1.isbn)

    def test_book_delete(self):
        self.assertEqual(3, Book.objects.all().count())
        url = reverse('api:book-detail', args=(self.book_1.id,))
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(2, Book.objects.all().count())


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(title='Test book 1', author='Author 1',
                                     year_published='2023-10-10', isbn='4129418247125')
        book_2 = Book.objects.create(title='Test book 2', author='Author 2',
                                     year_published='2023-10-11', isbn='8412491244891')
        book_3 = Book.objects.create(title='Test book 3', author='Author 3',
                                     year_published='2023-10-12', isbn='5012748219401')

        books = Book.objects.all()
        data = BookSerializer(books, many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'title': 'Test book 1',
                'author': 'Author 1',
                'year_published': '2023-10-10',
                'isbn': '4129418247125'
            },
            {
                'id': book_2.id,
                'title': 'Test book 2',
                'author': 'Author 2',
                'year_published': '2023-10-11',
                'isbn': '8412491244891'
            },
            {
                'id': book_3.id,
                'title': 'Test book 3',
                'author': 'Author 3',
                'year_published': '2023-10-12',
                'isbn': '5012748219401'
            }
        ]
        self.assertEqual(expected_data, data)
