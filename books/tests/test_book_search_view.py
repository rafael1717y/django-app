from unittest import skip

from django.urls import resolve, reverse

from books import views
from books.models import Book, Category, User

from .test_book_base import BookTestBase


class BookSearchViewTest(BookTestBase):
    def test_book_search_url_is_correct(self):
        url = reverse("books:search")
        self.assertEqual(url, "/books/search/")

    def test_book_search_uses_correct_view_function(self):
        resolved = resolve(reverse("books:search"))
        self.assertIs(resolved.func, views.search)

    def test_book_search_loads_correct_template(self):
        response = self.client.get(reverse("books:search") + "?q=teste")
        self.assertTemplateUsed(response, "books/pages/search.html")

    def test_book_search_raises_404_if_no_search_term(self):
        url = reverse("books:search")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_book_search_term_is_on_page_title_and_escaped(self):
        url = reverse("books:search") + "?q=<Teste>"
        response = self.client.get(url)
        self.assertIn(
            "Search for &quot;&lt;Teste&gt;&quot;", response.content.decode("utf-8")
        )

    @skip("in progress...")
    def test_book_search_can_find_book_by_title(self):
        title1 = "This is book one"
        title2 = "This is book two"

        book1 = self.make_book(
            slug="one", title=title1, author_data={"username": "one"}
        )
        book2 = self.make_book(
            slug="two", title=title2, author_data={"username": "two"}
        )

        search_url = reverse("books:search")
        response1 = self.client.get(f"{search_url}?q={title1}")
        response2 = self.client.get(f"{search_url}?q={title2}")
        response_both = self.client.get(f"{search_url}?q=this")

        self.assertIn(book1, response1.context["books"])
        self.assertNotIn(book2, response1.context["books"])

        self.assertIn(book2, response2.context["books"])
        self.assertNotIn(book1, response2.context["books"])

        self.assertIn(book1, response_both.context["books"])
        self.assertIn(book2, response_both.context["books"])
