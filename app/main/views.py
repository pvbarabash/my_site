from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    context = {
        'title': 'Букфрэш'
    }
    return render(request, 'main/index.html', context)
