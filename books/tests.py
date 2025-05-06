from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .models import Book, Borrow

# Create your tests here.

class BookModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            isbn='1234567890123',
            copies=5
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.author, 'Test Author')
        self.assertEqual(self.book.isbn, '1234567890123')
        self.assertEqual(self.book.copies, 5)

    def test_book_borrowing(self):
        # Test borrowing a book
        borrow = Borrow.objects.create(
            user=self.user,
            book=self.book,
            due_date=timezone.now() + timedelta(days=7)
        )
        
        # Check if book was borrowed
        self.assertEqual(borrow.user, self.user)
        self.assertEqual(borrow.book, self.book)
        self.assertFalse(borrow.returned)
        
        # Check if copies decreased
        self.book.refresh_from_db()
        self.assertEqual(self.book.copies, 4)

    def test_book_borrowing_no_copies(self):
        # Set copies to 0
        self.book.copies = 0
        self.book.save()
        
        # Try to borrow book
        with self.assertRaises(Exception):
            Borrow.objects.create(
                user=self.user,
                book=self.book,
                due_date=timezone.now() + timedelta(days=7)
            )
