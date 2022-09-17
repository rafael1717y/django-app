from django.urls import path

from books import views

# books:book
app_name = "books"

urlpatterns = [
    path("", views.home, name="home"),  # home
    path("books/search/", views.search, name="search"),
    path("books/category/<int:category_id>/", views.category, name="category"),
    path("books/<int:id>/", views.book, name="book"),  # books
    path("books", views.BookList.as_view(), name="book-list"),
]
