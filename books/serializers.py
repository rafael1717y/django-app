from rest_framework import serializers
from .models import Book


# API Rest - http://localhost:8000/books
"""Ex. Resposta para todos os campos
GET
 {
    "id": 1,
    "title": "Titulo",
    "description": "Descrição",
    "slug": "titulo",
    "book_author": "author",
    "publication_year": 11,
    "conservation_state": "MN",
    "language": "Português",
    "publishing_company": "São",
    "isbn": 1,
    "review": "dd",
    "review_is_html": false,
    "phoneNumber": "99393",
    "city": "São Paulo",
    "email": "rafaelufjf@gmail.com",
    "created_at": "2022-09-17T10:01:50.165246-03:00",
    "updated_at": "2022-09-17T10:01:50.165290-03:00",
    "is_published": true,
    "cover": "http://localhost:8000/media/books/covers/2022/09/17/code.jpg",
    "category": 1,
    "author": 1
  },

POST:
curl -X POST http://127.0.0.1:8000/books -H 'content-type: application/json' -d '{"title": "Teste API", "description": "descrição", "slug":"descri-1", "book_author":"rafael", "publication_year":1900, "conservation_state":"MN", "language":"português", "publishing_company": "Editora","isbn":"11", "review":"review","phoneNumber":"232","city":"SP"}'
"""

class BookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book
        fields = '__all__'
