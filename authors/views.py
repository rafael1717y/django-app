from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import RegisterForm


def register_view(request):
    """Redireciona para essa view após usuário criado."""
    register_form_data = request.session.get("register_form_data", None)
    form = RegisterForm(register_form_data)
    return render(
        request,
        "authors/pages/register_view.html",
        {
            "form": form,
        },
    )


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'Seu usuário foi criado, por favor realize o login.')
        del(request.session['register_form_data'])
    return redirect('authors:register')
