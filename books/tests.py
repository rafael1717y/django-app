from django.test import TestCase
from django.urls import reverse 


class BookURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        assert 1 == 1

    def test_books_home_url_is_correct(self):
        home_url = reverse('home')
        self.assertEqual(home_url, '/')
