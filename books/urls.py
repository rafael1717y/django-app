from django.urls import path
from books.views import home


urlpatterns = [
    path("", home), # home
]
