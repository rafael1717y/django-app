from django.shortcuts import render

from utils.books.factory import make_book
from books.models import Book


def home(request):
    books = Book.objects.all().order_by('-id')
    return render(
        request,
        "books/pages/home.html",
        context={
            "books": books},
    )


def book(request, id):
    return render(
        request,
        "books/pages/book-view.html",
        context={
            "book": make_book(),
            "is_detail_page": True,
        },
    )
