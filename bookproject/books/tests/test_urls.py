from django.core.urlresolvers import reverse, resolve
from django.test import TestCase


class TestBookURLs(TestCase):
    """Test URL patterns for books app."""

    def test_urls(self):
        self.assertEqual(reverse('books:index'), '/books/')
        self.assertEqual(
            reverse('books:detail', kwargs={'isbn': '123456'}),
            '/books/123456/')
        self.assertEqual(
            reverse('books:create'),
            '/books/create/')
        self.assertEqual(
            reverse('books:update', kwargs={'isbn': '123456'}),
            '/books/update/123456/')
        self.assertEqual(
            reverse('books:delete', kwargs={'isbn': '123456'}),
            '/books/delete/123456/')
        self.assertEqual(resolve('/books/').view_name, 'books:index')
        self.assertEqual(
            resolve('/books/123456/').view_name,
            'books:detail')
        self.assertEqual(
            resolve('/books/create/').view_name,
            'books:create')
        self.assertEqual(
            resolve('/books/update/123456/').view_name,
            'books:update')
        self.assertEqual(
            resolve('/books/delete/123456/').view_name,
            'books:delete')
        
