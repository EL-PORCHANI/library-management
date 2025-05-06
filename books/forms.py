from django import forms
from .models import Book, Reservation, Borrow
from datetime import timedelta, datetime

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'copies']

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        if len(isbn) != 13:
            raise forms.ValidationError("ISBN must be 13 characters.")
        return isbn

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['book']

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['book']

    def clean(self):
        cleaned_data = super().clean()
        book = cleaned_data.get('book')
        if book and book.copies < 1:
            raise forms.ValidationError("No copies available.")
        return cleaned_data