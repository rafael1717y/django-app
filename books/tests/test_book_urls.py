from django.test import TestCase
from django.urls import reverse


class BookURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        assert 1 == 1

    def test_book_home_url_is_correct(self):
        home_url = reverse("books:home")
        self.assertEqual(home_url, "/")

    def test_book_category_url_is_correct(self):
        url = reverse("books:category", kwargs={"category_id": 1})
        self.assertEqual(url, "/books/category/1/")

    def test_book_detail_url_is_correct(self):
        url = reverse("books:book", kwargs={"id": 1})
        self.assertEqual(url, "/books/1/")
