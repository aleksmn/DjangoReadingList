# from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.

def index(request):
    '''Render index page for Books'''
    books = Book.objects.all()
    # output = ', '.join([b.title for b in books])
    # return HttpResponse(output)
    return render(request, 'books/index.html', {'books': books})

def detail(request, book_id):
    '''Render detail page for Books'''
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/detail.html', {'book': book})

