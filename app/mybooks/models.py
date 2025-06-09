from tabnanny import verbose
from django.db import models
from users.models import User
from catalog.models import Books

class BookQueryset(models.QuerySet):
    ...

class UserBooks(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name = 'Пользователь')
    book = models.ForeignKey(to=Books, on_delete=models.CASCADE, verbose_name='Книга')
    status = models.CharField(max_length=20, choices=[('прочитано', 'Прочитано'), ('добавлено резюме', 'Добавлено резюме')])
    resume = models.TextField(blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    objects = BookQueryset().as_manager()


    class Meta:
        verbose_name = 'Книги пользователя'
        verbose_name_plural = 'Книги пользователя'

    def __str__ (self):
        return f'Корзина {self.user.username} | Книга {self.book.name}'