# Generated by Django 4.1 on 2022-10-22 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0007_rename_book_author_book_autor_do_livro"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="isbn",
            new_name="ANO_DE_PUBLICACAO",
        ),
        migrations.RenameField(
            model_name="book",
            old_name="city",
            new_name="CIDADE_DO_DOADOR",
        ),
        migrations.RenameField(
            model_name="book",
            old_name="publishing_company",
            new_name="EDITORA",
        ),
        migrations.RenameField(
            model_name="book",
            old_name="email",
            new_name="EMAIL_DO_DOADOR",
        ),
        migrations.RenameField(
            model_name="book",
            old_name="conservation_state",
            new_name="ESTADO_DE_CONSERVACAO",
        ),
        migrations.RenameField(
            model_name="book",
            old_name="language",
            new_name="IDIOMA",
        ),
        migrations.RenameField(
            model_name="book",
            old_name="cover",
            new_name="IMAGEM_DA_CAPA_DO_LIVRO",
        ),
        migrations.RenameField(
            model_name="book",
            old_name="publication_year",
            new_name="ISBN",
        ),
        migrations.RenameField(
            model_name="book",
            old_name="review",
            new_name="RESUMO_DA_OBRA",
        ),
        migrations.RenameField(
            model_name="book",
            old_name="phoneNumber",
            new_name="TELEFONE_DO_DOADOR",
        ),
        migrations.RenameField(
            model_name="book",
            old_name="titulo",
            new_name="TITULO",
        ),
    ]
