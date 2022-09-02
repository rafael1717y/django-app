from unittest import skip

from django.urls import resolve, reverse

from books import views
from books.models import Book, Category, User

from .test_book_base import BookTestBase


class BookCategoryViewTest(BookTestBase):
    def test_book_category_view_function_is_correct(self):
        view = resolve(reverse("books:category", kwargs={"category_id": 1000}))
        self.assertIs(view.func, views.category)

    def test_book_category_view_returns_404_if_no_books_found(self):
        response = self.client.get(
            reverse("books:category", kwargs={"category_id": 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_book_category_template_loads_books(self):
        needed_title = "This is a category test"
        # Need a recipe for this test
        self.make_book(title=needed_title)

        response = self.client.get(reverse("books:book", args=(1,)))
        content = response.content.decode("utf-8")

        # Check if one recipe exists
        self.assertIn(needed_title, content)

    def test_book_category_template_dont_load_books_not_published(self):
        """Test book is_published False dont show"""
        # Need a book for this test
        book = self.make_book(is_published=False)
        response = self.client.get(
            reverse("books:book", kwargs={"id": book.category.id})
        )
        self.assertEqual(response.status_code, 404)
