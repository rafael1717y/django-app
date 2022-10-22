from django.contrib import admin

from .models import Book, Category


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "TITULO",
        "created_at",
        "AUTOR_DO_LIVRO",
        "is_published",
        "ANO_DE_PUBLICACAO",
    ]
    list_display_links = "TITULO", "created_at"
    search_fields = (
        "id",
        "TITULO",
        "DESCRICAO",
        "AUTOR_DO_LIVRO",
        "slug",
        "ANO_DE_PUBLICACAO",
    )
    list_filter = "category", "author", "is_published", "review_is_html"
    list_per_page = 7
    list_editable = ("is_published",)
    ordering = ("-id",)
    prepopulated_fields = {"slug": ("TITULO",)}


admin.site.register(Category, CategoryAdmin)
