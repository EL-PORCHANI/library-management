from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reserved_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} reserved {self.book.title}"

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"