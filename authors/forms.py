from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, "")
    field.widget.attrs[attr_name] = f"{existing} {attr_new_val}".strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, "placeholder", placeholder_val)


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields["username"], "Seu nome de usuário")
        add_placeholder(self.fields["email"], "Seu email")
        add_placeholder(self.fields["first_name"], "Ex.: John")
        add_placeholder(self.fields["last_name"], "Ex.: Doe")
        add_attr(self.fields["username"], "css", "a-css-class")

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Sua senha"}),
        error_messages={"required": "O campo senha não pode ser vazio."},
        help_text=(
            "A senha deve ter ao menos um caractere maiúsculo, "
            "uma letra minúscula e um número. O tamanho não pode ser menor que 8 caracteres."
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Repita sua senha"}),
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
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Digite seu primeiro nome aqui.",
                    "class": "input text-input",
                }
            ),
            "password": forms.PasswordInput(
                attrs={"placeholder": "Digite sua senha aqui."}
            ),
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
