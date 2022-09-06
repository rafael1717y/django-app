from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from books.models import Book

from .forms import LoginForm, RegisterForm


def register_view(request):
    """Redireciona para essa view após usuário criado."""
    register_form_data = request.session.get("register_form_data", None)
    form = RegisterForm(register_form_data)
    return render(
        request,
        "authors/pages/register_view.html",
        {
            "form": form,
            "form_action": reverse("authors:register_create"),
        },
    )


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session["register_form_data"] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, "Seu usuário foi criado, por favor realize o login.")
        del request.session["register_form_data"]
        return redirect(reverse("authors:login"))
    return redirect("authors:register")


def login_view(request):
    form = LoginForm()
    return render(
        request,
        "authors/pages/login.html",
        {"form": form, "form_action": reverse("authors:login_create")},
    )


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    login_url = reverse("authors:login")

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get("username", ""),
            password=form.cleaned_data.get("password", ""),
        )

        if authenticated_user is not None:
            messages.success(request, "Você está logado.")
            login(request, authenticated_user)
        else:
            messages.error(request, "Credenciais inválidas")
    else:
        messages.error(request, "Nome de usuário ou senha inválidas.")

    return redirect(reverse("authors:dashboard"))


@login_required(login_url="authors:login", redirect_field_name="next")
def logout_view(request):
    """View de logout é logout_view difrente da função logout."""
    if not request.POST:
        return redirect(reverse("authors:login"))

    if request.POST.get("username") != request.user.username:
        print("Invalid user name", request.POST, request.user)
        return redirect(reverse("authors:login"))

    logout(request)
    return redirect(reverse("authors:login"))


@login_required(login_url="authors:login", redirect_field_name="next")
def dashboard(request):
    books = Book.objects.filter(is_published=False, author=request.user)
    return render(
        request,
        "authors/pages/dashboard.html",
        context={
            "books": books,
        },
    )


@login_required(login_url="authors:login", redirect_field_name="next")
def dashboard_book_edit(request, id):
    book = Book.objects.filter(
        is_published=False,
        author=request.user,
        pk=id,
    )

    if not book:
        raise Http404()

    return render(request, "authors/pages/dashboard_book.html", context={})
