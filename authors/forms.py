from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, "")
    field.widget.attrs[attr_name] = f"{existing} {attr_new_val}".strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, "placeholder", placeholder_val)


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'A senha deve ter ao menos um caractere maiúsculo, '
            'um minúsculo e um número. O tamanho deve ser de'
            'ao menos 8 caracteres.'
        ),
            code='invalid'
        )

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields["username"], "Seu nome de usuário")
        add_placeholder(self.fields["email"], "Seu email")
        add_placeholder(self.fields["first_name"], "Ex.: John")
        add_placeholder(self.fields["last_name"], "Ex.: Doe")
        add_placeholder(self.fields['password'], 'Digite sua senha')
        add_placeholder(self.fields['password2'], 'Repita sua senha')


    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        error_messages={"required": "O campo senha não pode ser vazio."},
        help_text=(
            "A senha deve ter ao menos um caractere maiúsculo, "
            "uma letra minúscula e um número. O tamanho não pode ser menor que 8 caracteres."
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]
        # exclude = ['first_name']
        labels = {
            "username": "Nome de usuário",
            "first_name": "Primeiro nome",
            "last_name": "Último nome",
            "email": "E-mail",
            "password": "Senha",
        }
        help_texts = {
            "email": "O email deve ser válido",
        }
        error_messages = {
            "username": {
                "required": "Este campo não pode ser vazio.",
            }
        }
       

    def clean_password(self):
        data = self.cleaned_data.get("password")

        if "atenção" in data:
            raise ValidationError(
                "Não digite %(pipoca)s no campo password",
                code="invalid",
                params={"pipoca": '"atenção"'},
            )

        return data

    def clean_first_name(self):
        data = self.cleaned_data.get("first_name")

        if "John Doe" in data:
            raise ValidationError(
                "Não digite %(value)s no campo first name",
                code="invalid",
                params={"value": '"John Doe"'},
            )

        return data

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Password and password2 devem ser iguais',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })
