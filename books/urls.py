from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_book, name='add_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('reserve/<int:book_id>/', views.reserve_book, name='reserve_book'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('history/', views.borrowing_history, name='borrowing_history'),
    path('check-overdue/', views.check_overdue, name='check_overdue'),
    path('api/books/', views.BookListCreate.as_view(), name='book-list-create'),
] 