from django.test import TestCase

from books import views
from books.models import Book, Category, User


class BookMixin:
    def make_category(self, name="Category"):
        return Category.objects.create(name=name)

    def make_author(
        self,
        first_name="user",
        last_name="name",
        username="username",
        password="123456",
        email="username@email.com",
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_book(
        self,
        category_data=None,
        author_data=None,
        title="Título do Livro",
        description="Descrição do livro",
        slug="book-slug",
        publication_year="1980",
        conservation_state="U",
        language="português",
        publishing_company="editora",
        isbn="1234",
        review="review",
        review_is_html=True,
        is_published=True,
        phoneNumber="+234343433434",
        email="rafael@gmail.com",
    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Book.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            publication_year=publication_year,
            conservation_state=conservation_state,
            language=language,
            publishing_company=publishing_company,
            isbn=isbn,
            review=review,
            review_is_html=review_is_html,
            is_published=is_published,
            phoneNumber=phoneNumber,
            email=email,
        )

    def make_book_in_batch(self, qtd=10):
        books = []
        for i in range(qtd):
            kwargs = {
                "slug": f"r{i}",
                "author_data": {"username": f"u{i}", "email": f"e{i}@gmail.com"},
            }
            book = self.make_book(**kwargs)
            books.append(book)
        return books


class BookTestBase(TestCase, BookMixin):
    def setUp(self):
        return super().setUp()
