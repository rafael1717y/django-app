from books.models import Book
from django import forms
from utils.django_forms import add_attr
from collections import defaultdict
from django.core.exceptions import ValidationError



class AuthorBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)
        

        add_attr(self.fields.get('title'), 'class', 'span-2')
        
        
        

    class Meta:
        model = Book
        fields = 'title', 'description', 'book_author', \
            'publication_year', 'conservation_state', \
                'language', 'publishing_company', \
                'isbn', 'review', 'email', 'cover'
        widgets = {
            'cover' : forms.FileInput(
                attrs= {
                    'class': 'span-2'
                }
            ),
            'language': forms.Select(
                choices=(
                    ('Português', 'Português'),
                    ('Inglês', 'Inglês'),
                    ('Espanhol', 'Espanhol'),
                    ('Francês', 'Francês'),
                    ('Alemão', 'Alemão'),
                    ('Italiano', 'Italiano'),
                ),
            ),
        }


    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        cd = self.cleaned_data
        title = cd.get('title')
        description = cd.get('description')
        if len(title) < 5:
            self._my_errors['title'].append('Título deve ter ao menos 5 caracteres.')

        if title == description:
            self._my_errors['title'].append('Não pode ser igual a descrição')
            self._my_errors['description'].append('Não pode ser igual ao título')

        if self._my_errors: 
            raise ValidationError(self._my_errors)

        return super_clean


