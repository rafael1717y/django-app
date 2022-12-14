# Generated by Django 4.1 on 2022-10-22 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0008_rename_isbn_book_ano_de_publicacao_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="ESTADO_DE_CONSERVACAO",
            field=models.CharField(
                choices=[
                    ("Muito Usado", "Muito Usado"),
                    ("Usado", "Usado"),
                    ("Semi-novo", "Semi-Novo"),
                    ("Novo", "Novo"),
                ],
                max_length=20,
            ),
        ),
    ]
