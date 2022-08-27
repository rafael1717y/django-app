from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"), # home
    path('books/<int:id>/', views.book), # books
]
