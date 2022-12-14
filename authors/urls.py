from django.urls import path

from . import views

app_name = "authors"

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("register/create/", views.register_create, name="register_create"),
    path("login/", views.login_view, name="login"),
    path("login/create/", views.login_create, name="login_create"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('dashboard/book/new/', 
         views.dashboard_book_new, 
         name='dashboard_book_new'),
    path(
        "dashboard/book/<int:id>/edit/",
        views.dashboard_book_edit,
        name="dashboard_book_edit",
    ),
    path(
        "dashboard/book/<int:id>/delete/",
        views.dashboard_book_delete,
        name="dashboard_book_delete",
    ),
]
