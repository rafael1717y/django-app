from django.db import models
from django.contrib.auth.models import User 

"""
class Category(models.Model):
    name = models.CharField(max_length=65)


class Book(models.Model):
    CONSERVATION_CHOICES = (
        ('MN', 'Muito Usado'),
        ("U", 'Usado'),
        ('SN', 'Semi-Novo'),
        ('N', 'Novo')
    )
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    book_author = models.CharField(max_length=65)
    publication_year = models.IntegerField()
    conservation_state = models.CharField(max_length=2, choices=CONSERVATION_CHOICES, blank=False, null= False)
    available = models.BooleanField()  # livro já doado ou não
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    #phone = models.
    email = models.EmailField(max_length=70,blank=True,unique=True)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
"""

"""
pip install django-phonenumber-field
TABELAS ----

title
description
slug
author do livro
data de criação
data de atualização
ano
estado - novo, semi-novo, usado, muito usado 
capa

----------
category (Relação)
Doador (author) (Relação)
Doador - fone
Doador - email
"""

