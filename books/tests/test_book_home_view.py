from unittest import skip
from unittest.mock import patch

from django.urls import resolve, reverse

from books import views
from books.models import Book, Category, User

from .test_book_base import BookTestBase


class BookHomeViewTest(BookTestBase):
    def tearDown(self) -> None:
        return super().tearDown()

    def test_book_home_view_function_is_correct(self):
        view = resolve(reverse("books:home"))
        self.assertIs(view.func, views.home)

    # 1
    # @skip("WIP")
    def test_book_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse("books:home"))
        self.assertEqual(response.status_code, 200)

    # 2
    # @skip("WIP")
    def test_book_home_view_loads_correct_template(self):
        response = self.client.get(reverse("books:home"))
        self.assertTemplateUsed(response, "books/pages/home.html")

    # 3
    # @skip("WIP")
    def test_book_home_template_shows_no_books_found_if_no_books(self):
        response = self.client.get(reverse("books:home"))
        self.assertIn(
            "<h1>No books found here 🥲</h1>", response.content.decode("utf-8")
        )

    def test_book_home_template_loads_books(self):
        self.make_book()
        response = self.client.get(reverse("books:home"))
        content = response.content.decode("utf-8")
        response_context_books = response.context["books"]
        self.assertIn("Título do Livro", content)
        self.assertIn("Descrição do livro", content)
        self.assertEqual(len(response_context_books), 1)

    def test_book_home_template_dont_load_books_not_published(self):
        """Test book is_published False dont show"""
        # Need a book for this test
        self.make_book(is_published=False)
        response = self.client.get(reverse("books:home"))
        self.assertIn(
            "<h1>No books found here 🥲</h1>", response.content.decode("utf-8")
        )

    def test_book_home_is_paginated(self):
        for i in range(8):
            kwargs = {"slug": f"r{i}", "book_author": {"username": f"u{i}"}}
            self.make_book(**kwargs)

        with patch("books.views.PER_PAGE", new=3):
            response = self.client.get(reverse("books:home"))
            books = response.context["books"]
            paginator = books.paginator

            self.assertEqual(paginator.num_pages, 3)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)
            self.assertEqual(len(paginator.get_page(3)), 2)
