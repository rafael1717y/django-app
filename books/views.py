from django.shortcuts import render


def home(request):
    return render(request, 'books/pages/home.html', context={
        'name': 'Grupo PI',
    })

def book(request, id):
    return render(request, 'books/pages/book-view.html', context={
        'name': 'Grupo PI',
    })

