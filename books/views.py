from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from rest_framework import generics
from .models import Book, Reservation, Borrow
from .forms import BookForm, ReservationForm, BorrowForm
from .serializers import BookSerializer

# API Views
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Regular Views
def home(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('home')
    return render(request, 'books/delete_book.html', {'book': book})

@login_required
def reserve_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.book = book
            reservation.save()
            messages.success(request, 'Book reserved successfully!')
            return redirect('home')
    else:
        form = ReservationForm()
    return render(request, 'books/reserve_book.html', {'form': form, 'book': book})

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            if book.copies > 0:
                borrow = form.save(commit=False)
                borrow.user = request.user
                borrow.book = book
                borrow.due_date = timezone.now() + timedelta(days=7)
                borrow.save()
                book.copies -= 1
                book.save()
                messages.success(request, 'Book borrowed successfully!')
                return redirect('home')
            else:
                messages.error(request, 'No copies available for borrowing.')
    else:
        form = BorrowForm()
    return render(request, 'books/borrow_book.html', {'form': form, 'book': book})

@login_required
def borrowing_history(request):
    borrows = Borrow.objects.filter(user=request.user).order_by('-borrow_date')
    return render(request, 'books/history.html', {'borrows': borrows})

@login_required
def check_overdue(request):
    overdue_borrows = Borrow.objects.filter(
        user=request.user,
        due_date__lt=timezone.now(),
        returned=False
    )
    if overdue_borrows.exists():
        messages.warning(request, f'You have {overdue_borrows.count()} overdue book(s)!')
    else:
        messages.success(request, 'No overdue books!')
    return redirect('home')
