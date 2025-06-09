from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from mybooks.models import UserBooks 
from catalog.models import Books
# from mybooks.forms import UserBookForm


def mybooks(request):
    userbooks = UserBooks.objects.filter(user=request.user)
    context = {
        'title': 'Мои книги',
        'books': userbooks,
    }
    return render(request, 'mybooks/mybooks.html', context)


def book_add(request):
    book_id = request.POST.get("book_id")
    book = Books.objects.get(id=book_id)
    
    UserBooks.objects.create(user=request.user, book=book, status='прочитано')


    response_data = {
        "message": "Книга добавлена в прочитанные",
    }

    return JsonResponse(response_data)




# def add_user_book(request):
#     if request.method == 'POST':
#         form = UserBookForm(request.POST)
#         if form.is_valid():
#             user_book = form.save(commit=False)
#             if user_book.status == 'read' and not user_book.resume:
#                 form.add_error('resume', 'Резюме обязательно для прочитанных книг.')
#             else:
#                 user_book.user = request.user
#                 user_book.save()
#                 return redirect('mybooks:mybooks')
#     else:
#         form = UserBookForm()
    
#     context = {
#         'title': 'Добавление книги',
#         'form': form
#     }

#     return render(request, 'add_user_book.html', context)