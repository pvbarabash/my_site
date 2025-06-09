from django.shortcuts import render
from catalog.models import Books


def catalog(request):
    books = Books.objects.all()
    context = {
        'title': 'Каталог',
        'books': books,
    }
    return render(request, 'catalog/catalog.html', context)

