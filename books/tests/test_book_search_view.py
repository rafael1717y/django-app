from django.urls import resolve, reverse

from books import views

from .test_book_base import BookTestBase


class BookSearchViewsTest(BookTestBase):
    def test_book_search_url_is_correct(self):
        url = reverse("books:search")
        self.assertEqual(url, "/books/search/")

    def test_book_search_uses_correct_view_function(self):
        resolved = resolve(reverse("books:search"))
        self.assertIs(resolved.func, views.search)

    def test_book_search_loads_correct_template(self):
        response = self.client.get(reverse("books:search"))
        self.assertTemplateUsed(response, "books/pages/search.html")

    def test_book_search_raises_404_if_no_search_term(self):
        url = reverse("books:search")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_book_search_term_is_on_page_title_and_escaped(self):
        url = reverse("books:search") + "?search=<Teste>"
        response = self.client.get(url)
        self.assertIn(
            "Search for &quot;&lt;Teste&gt;&quot;", response.content.decode("utf-8")
        )
