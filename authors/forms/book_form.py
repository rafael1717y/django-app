from books.models import Book
from django import forms
from utils.django_forms import add_attr
from collections import defaultdict
from django.core.exceptions import ValidationError



class AuthorBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)
        

        add_attr(self.fields.get('TITULO'), 'class', 'span-2')
        
        
        

    class Meta:
        model = Book
        fields = 'TITULO', 'DESCRICAO', 'AUTOR_DO_LIVRO', \
            'ANO_DE_PUBLICACAO', 'ESTADO_DE_CONSERVACAO', \
            'IDIOMA', 'EDITORA', 'category', \
            'ISBN', 'RESUMO_DA_OBRA','CIDADE_DO_DOADOR', \
            'EMAIL_DO_DOADOR','TELEFONE_DO_DOADOR', 'IMAGEM_DA_CAPA_DO_LIVRO',                
        widgets = {
            'IMAGEM_DA_CAPA_DO_LIVRO' : forms.FileInput(
                attrs= {
                    'class': 'span-2'
                }
            ),
            'IDIOMA': forms.Select(
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
        TITULO = cd.get('TITULO')
        description = cd.get('DESCRICAO')
        if len(TITULO) < 5:
            self._my_errors['TITULO'].append('Título deve ter ao menos 5 caracteres.')

        if TITULO == description:
            self._my_errors['TITULO'].append('Não pode ser igual a descrição')
            self._my_errors['DESCRICAO'].append('Não pode ser igual ao título')

        if self._my_errors: 
            raise ValidationError(self._my_errors)

        return super_clean


