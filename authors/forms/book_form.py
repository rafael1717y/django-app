from books.models import Book
from django import forms


class AuthorBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = 'title', 'description', 'book_author', \
            'publication_year', 'conservation_state', \
                'language', 'publishing_company', \
                'review', 'cover'
