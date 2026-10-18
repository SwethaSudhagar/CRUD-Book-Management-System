from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

# Read all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})

# Create a new book
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        Book.objects.create(
            title=title,
            author=author,
            price=price
        )
        return redirect('book_list')

    return render(request, 'book/add_book.html')

# Update book price
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.price = request.POST.get('price')
        book.save()
        return redirect('book_list')

    return render(request, 'book/update_book.html', {'book': book})

# Delete a book
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'book/delete_book.html', {'book': book})
    
