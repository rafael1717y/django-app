# Generated by Django 4.1 on 2022-10-22 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0009_alter_book_estado_de_conservacao"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Category",
            new_name="CATEGORIA",
        ),
        migrations.RenameField(
            model_name="book",
            old_name="category",
            new_name="CATEGORIA",
        ),
    ]