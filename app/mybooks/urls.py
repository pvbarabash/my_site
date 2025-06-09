from django.urls import path

from mybooks import views

app_name = 'mybooks'

urlpatterns = [
    path('', views.mybooks, name='mybooks'),
    path('book_add/', views.book_add, name='book_add')
]
