import os

from django.contrib import messages
from django.db.models import Q
from django.http.response import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from utils.books.factory import make_book
from utils.pagination import make_pagination

from .models import Book
from rest_framework import generics
from .serializers import BookSerializer


PER_PAGE = int(os.environ.get("PER_PAGE", 3))

# Api

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



def home(request):
    books = Book.objects.filter(
        is_published=True,
    ).order_by("-id")

    page_obj, pagination_range = make_pagination(request, books, PER_PAGE)

    return render(
        request,
        "books/pages/home.html",
        context={"books": page_obj, "pagination_range": pagination_range
        })


def category(request, category_id):
    books = get_list_or_404(
        Book.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by("-id")
    )

    page_obj, pagination_range = make_pagination(request, books, PER_PAGE)

    return render(
        request,
        "books/pages/category.html",
        context={
            "books": page_obj,
            "pagination_range": pagination_range,
            "title": f"{books[0].category.name} - Category | ",
        })


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
            Q(TITULO__icontains=search_term) | Q(DESCRICAO__icontains=search_term),
        ),
        is_published=True,
    ).order_by("-id")

    page_obj, pagination_range = make_pagination(request, books, PER_PAGE)

    #messages.success(request, "Epa, voc?? pesquisou!!!.")
    return render(
        request,
        "books/pages/search.html",
        {
            "page_title": f'Search for "{search_term}" |',
            "search_term": search_term,
            "books": page_obj,
            "pagination_range": pagination_range,
            "additional_url_query": f"&q={search_term}",
        },
    )
