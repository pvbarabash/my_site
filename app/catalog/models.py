from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog_images', blank=True, null=True)


    class Meta:
        db_table = 'book'
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'

    def __str__ (self):
        return self.name