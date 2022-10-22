from unittest import skip

from django.urls import resolve, reverse

from books import views
from books.models import Book, Category, User

from .test_book_base import BookTestBase


class BookDetailView(BookTestBase):
    def test_book_detail_view_function_is_correct(self):
        view = resolve(reverse("books:book", kwargs={"id": 1}))
        self.assertIs(view.func, views.book)

    def test_book_detail_view_returns_404_if_no_books_found(self):
        response = self.client.get(reverse("books:book", kwargs={"id": 1000}))
        self.assertEqual(response.status_code, 404)

    def test_book_detail_template_loads_the_correct_book(self):
        needed_title = "This is a detail page - It load one book"

        # Need a recipe for this test
        self.make_book(TITULO=needed_title)

        response = self.client.get(reverse("books:book", kwargs={"id": 1}))
        content = response.content.decode("utf-8")
        # Verifica se um livro existe
        self.assertIn(needed_title, content)

    def test_book_detail_template_dont_load_book_not_published(self):
        """Test book is_published False dont show"""
        # Need a recipe for this test
        book = self.make_book(is_published=False)

        response = self.client.get(reverse("books:book", kwargs={"id": book.id}))

        self.assertEqual(response.status_code, 404)

    def test_book_detail_template_dont_load_book_not_published(self):
        """Test book is_published False dont show"""
        # Need a book for this test
        book = self.make_book(is_published=False)
        response = self.client.get(reverse("books:book", kwargs={"id": book.id}))
        self.assertEqual(response.status_code, 404)
