from unittest import skip

from django.urls import resolve, reverse

from books import views
from books.models import Book, Category, User

from .test_book_base import BookTestBase


class BookViewsTest(BookTestBase):
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

    def test_book_category_view_function_is_correct(self):
        view = resolve(reverse("books:category", kwargs={"category_id": 1000}))
        self.assertIs(view.func, views.category)

    def test_book_category_view_returns_404_if_no_books_found(self):
        response = self.client.get(
            reverse("books:category", kwargs={"category_id": 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_book_detail_view_function_is_correct(self):
        view = resolve(reverse("books:book", kwargs={"id": 1}))
        self.assertIs(view.func, views.book)

    def test_book_detail_view_returns_404_if_no_books_found(self):
        response = self.client.get(reverse("books:book", kwargs={"id": 1000}))
        self.assertEqual(response.status_code, 404)

    def test_book_home_template_loads_books(self):
        self.make_book()
        response = self.client.get(reverse("books:home"))
        content = response.content.decode("utf-8")
        response_context_books = response.context["books"]
        self.assertIn("Título do Livro", content)
        self.assertIn("Descrição do livro", content)
        self.assertEqual(len(response_context_books), 1)

    def test_book_category_template_loads_books(self):
        needed_title = "This is a category test"
        # Need a recipe for this test
        self.make_book(title=needed_title)

        response = self.client.get(reverse("books:book", args=(1,)))
        content = response.content.decode("utf-8")

        # Check if one recipe exists
        self.assertIn(needed_title, content)

    def test_book_detail_template_loads_the_correct_book(self):
        needed_title = "This is a detail page - It load one book"

        # Need a recipe for this test
        self.make_book(title=needed_title)

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

    def test_book_home_template_dont_load_books_not_published(self):
        """Test book is_published False dont show"""
        # Need a book for this test
        self.make_book(is_published=False)
        response = self.client.get(reverse("books:home"))
        self.assertIn(
            "<h1>No books found here 🥲</h1>", response.content.decode("utf-8")
        )

    def test_book_category_template_dont_load_books_not_published(self):
        """Test book is_published False dont show"""
        # Need a book for this test
        book = self.make_book(is_published=False)
        response = self.client.get(
            reverse("books:book", kwargs={"id": book.category.id})
        )
        self.assertEqual(response.status_code, 404)

    def test_book_detail_template_dont_load_book_not_published(self):
        """Test book is_published False dont show"""
        # Need a book for this test
        book = self.make_book(is_published=False)
        response = self.client.get(reverse("books:book", kwargs={"id": book.id}))
        self.assertEqual(response.status_code, 404)

    def test_book_search_url_is_correct(self):
        url = reverse("books:search")
        self.assertEqual(url, "/books/search/")

    def test_book_search_uses_correct_view_function(self):
        resolved = resolve(reverse("books:search"))
        self.assertIs(resolved.func, views.search)

    def test_book_search_loads_correct_template(self):
        response = self.client.get(reverse("books:search"))
        self.assertTemplateUsed(response, "books/pages/search.html")
