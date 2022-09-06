from django.contrib import admin

from .models import Book, Category


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "created_at",
        "book_author",
        "is_published",
        "publication_year",
    ]
    list_display_links = "title", "created_at"
    search_fields = (
        "id",
        "title",
        "description",
        "book_author",
        "slug",
        "publication_year",
    )
    list_filter = "category", "author", "is_published", "review_is_html"
    list_per_page = 7
    list_editable = ("is_published",)
    ordering = ("-id",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
