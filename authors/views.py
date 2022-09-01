from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import Http404


def register_view(request):
    """Redireciona para essa view após usuário criado."""
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)    
    return render(request, "authors/pages/register_view.html", {
        'form': form,
    })

def register_create(request):
    """Criação de um registro"""
    if not request.POST:
        raise Http404()
    
    POST = request.POST 
    request.session['register_form_data'] = POST 
    form = RegisterForm(POST)    

    return redirect('authors:register')
