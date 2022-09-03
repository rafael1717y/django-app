from django.test import TestCase
from parameterized import parameterized

from authors.forms import RegisterForm


class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand(
        [
            ("username", "Seu nome de usuário"),
            ("email", "Seu email"),
            ("first_name", "Ex.: John"),
            ("last_name", "Ex.: Doe"),
            ("password", "Digite sua senha"),
            ("password2", "Repita sua senha"),
        ]
    )
    def test_first_name_placeholder_is_correct(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs["placeholder"]
        self.assertEqual(current_placeholder, placeholder)
