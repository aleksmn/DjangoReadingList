from django.contrib import admin
from .models import Genre, Book

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class BookAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('title', 'author', 'genre', 'rating')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)