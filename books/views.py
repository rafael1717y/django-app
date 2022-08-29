from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from utils.books.factory import make_book

from .models import Book


def home(request):
    books = Book.objects.filter(
        is_published=True,
    ).order_by("-id")

    if not books:
        raise Http404("Not found 🥲")

    return render(
        request,
        "books/pages/home.html",
        context={
            "books": books,
            "title": f"{books.first().category.name} - Category | ",
        },
    )


def category(request, category_id):
    books = get_list_or_404(
        Book.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by("-id")
    )

    return render(
        request,
        "books/pages/category.html",
        context={"books": books, "title": f"{books[0].category.name} - Category | "},
    )


def book(request, id):
    book = get_object_or_404(
        Book,
        pk=id,
        is_published=True,
    )

    return render(
        request,
        "books/pages/book-view.html",
        context={
            "book": book,
            "is_detail_page": True,
        },
    )
