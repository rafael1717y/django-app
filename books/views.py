from django.db.models import Q
from django.http.response import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.contrib import messages
from utils.books.factory import make_book

from .models import Book


def home(request):
    books = Book.objects.filter(
        is_published=True,
    ).order_by("-id")

    return render(
        request,
        "books/pages/home.html",
        context={
            "books": books,
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


def search(request):
    search_term = request.GET.get("q", "").strip()

    if not search_term:
        raise Http404()

    books = Book.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')
    messages.success(request, 'Epa, você pesquisou!!!.')
    return render(
        request,
        "books/pages/search.html",
        {
            "page_title": f'Search for "{search_term}" |',
            "search_term": search_term,
            "books": books,
        },
    )
