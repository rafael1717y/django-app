from django.urls import path

from . import views

# books:book
app_name = "books"

urlpatterns = [
    path("", views.home, name="home"),  # home
    path("books/<int:id>/", views.book, name="book"),  # books
]
