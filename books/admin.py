from django.contrib import admin

from .models import Book, Category


class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Book)    
class BookAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)

