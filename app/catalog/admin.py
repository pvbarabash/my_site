from django.contrib import admin
from catalog.models import Books

# Register your models here.

#admin.site.register(Books)

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',)}
