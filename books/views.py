from django.shortcuts import render

from utils.books.factory import make_book


def home(request):
    return render(
        request,
        "books/pages/home.html",
        context={"books": [make_book() for _ in range(10)]},
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
