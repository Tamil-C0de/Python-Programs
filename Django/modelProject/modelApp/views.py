from django.shortcuts import render
from .models import Book

def add_book(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        publication_date = request.POST['publication_date']
        price = request.POST['price']
        stock = request.POST['stock']
        
        new_book = Book(
            title=title,
            author=author,
            publication_date=publication_date,
            price=price,
            stock=stock
        )
        new_book.save()
    return render(request, 'modelApp/add_book.html')