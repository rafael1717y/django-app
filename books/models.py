from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify


class Category(models.Model):
    """Representa a categoria de um livro. Ex. literatura
    estrangeira, livro técnico...
    """

    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Livros"""

    CONSERVATION_CHOICES = (
        ("Muito Usado", "Muito Usado"),
        ("Usado", "Usado"),
        ("Semi-novo", "Semi-Novo"),
        ("Novo", "Novo"),
    )
    TITULO = models.CharField(max_length=65)
    DESCRICAO = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    AUTOR_DO_LIVRO = models.CharField(max_length=65)
    ANO_DE_PUBLICACAO = models.IntegerField()
    ESTADO_DE_CONSERVACAO = models.CharField(
        max_length=20, choices=CONSERVATION_CHOICES, blank=False, null=False
    )
    IDIOMA = models.CharField(max_length=50)
    EDITORA = models.CharField(max_length=65)
    ISBN = models.IntegerField()
    RESUMO_DA_OBRA = models.TextField() #review
    review_is_html = models.BooleanField(default=False)
    TELEFONE_DO_DOADOR = models.CharField(max_length=15)
    CIDADE_DO_DOADOR = models.CharField(max_length=30)
    EMAIL_DO_DOADOR = models.EmailField(max_length=70, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    IMAGEM_DA_CAPA_DO_LIVRO = models.ImageField(
        upload_to="books/covers/%Y/%m/%d/", blank=True, default=""
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.TITULO


    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.TITULO)}'
            self.slug = slug

        return super().save(*args, **kwargs)
