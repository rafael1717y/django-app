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
        ("MN", "Muito Usado"),
        ("U", "Usado"),
        ("SN", "Semi-Novo"),
        ("N", "Novo"),
    )
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    book_author = models.CharField(max_length=65)
    publication_year = models.IntegerField()
    conservation_state = models.CharField(
        max_length=2, choices=CONSERVATION_CHOICES, blank=False, null=False
    )
    language = models.CharField(max_length=50)
    publishing_company = models.CharField(max_length=65)
    isbn = models.IntegerField()
    review = models.TextField()
    review_is_html = models.BooleanField(default=False)
    phoneNumber = models.CharField(max_length=15)
    city = models.CharField(max_length=30)
    email = models.EmailField(max_length=70, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to="books/covers/%Y/%m/%d/", blank=True, default=""
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.title)}'
            self.slug = slug

        return super().save(*args, **kwargs)
