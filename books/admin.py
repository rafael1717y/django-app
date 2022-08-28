from django.contrib import admin
from .models import Category, Book


class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Book)    
class BookAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)

