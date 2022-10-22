from unittest import skip

from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_book_base import BookTestBase


class BookModelTest(BookTestBase):
    def setUp(self):
        self.book = self.make_book()
        return super().setUp()

    # 1
    def test_book_title_raises_error_if_title_has_more_65_chars(self):
        self.book.TITULO = "A" * 70
        with self.assertRaises(ValidationError):
            self.book.full_clean()  # Aqui a validação ocorre - levanta exceção aqui
            self.book.save()
            # self.fail(self.book.title)

    @parameterized.expand(
        [
            ("TITULO", 65),
            ("DESCRICAO", 200),
            ("AUTOR_DO_LIVRO", 65),
            ("IDIOMA", 50),
            ("EDITORA", 65),
        ]
    )
    def test_book_fields_max_length(self, field, max_length):
        setattr(self.book, field, "A" * (max_length + 5))
        with self.assertRaises(ValidationError):
            self.book.full_clean()

    @skip("WIP")
    def test_book_string_representation(self):
        needed = "Testing Representation"
        self.book.TITULO = needed
        self.book_author = "Rafael"
        self.phoneNumber = "+23456798090"
        self.book.full_clean()
        self.book.save()
        self.assertEqual(
            str(self.book),
            needed,
            msg=f"book string representation must be "
            f'"{needed}" but "{str(self.book)}" was received.',
        )
