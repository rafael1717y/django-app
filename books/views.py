from django.shortcuts import render


def home(request):
    return render(request, 'books/pages/home.html', context={
        'name': 'Grupo PI',
    })



