from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import RegisterForm
from django.urls import reverse 
from django.contrib.auth import authenticate, login
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
            'form_action': reverse('authors:register_create'),
        })


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Seu usuário foi criado, por favor realize o login.')
        del(request.session['register_form_data'])
    return redirect('authors:register')


def login_view(request):
    form = LoginForm()
    return render(request, 'authors/pages/login.html', {
        'form': form,
        'form_action': reverse('authors:login_create')
    })
    


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    login_url = reverse('authors:login')

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Você está logado.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Credenciais inválidas')
    else:
        messages.error(request, 'Nome de usuário ou senha inválidas.')

    return redirect(login_url)
