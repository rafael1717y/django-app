from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'books/home.html')



def contato(request):
    return render(request, 'books/contato.html')


def sobre(request):
        return HttpResponse('Sobre')
