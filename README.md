# Library Management System

A Django-based library management system that allows users to manage books, handle reservations, track borrowing history, and receive notifications for overdue books.

## Features

- Book Management
  - Add new books with title, author, ISBN, and number of copies
  - Delete books
  - List all books with their details
- Reservation System
  - Users can reserve books
- Borrowing System
  - Users can borrow books (reduces available copies)
  - Track borrowing history (user, book, borrow date, due date, return status)
- Overdue Notifications
  - Notify users when borrowed books are overdue
- User Authentication
  - Login/logout functionality
  - Protected routes for authenticated users
- REST API
  - List and create books
  - Testable with Postman

## Technologies Used

- Django 4.x
- Django REST Framework
- Bootstrap 5
- PostgreSQL (Heroku)
- SQLite (local development)
- Beekeeper Studio
- Postman
- Heroku
- Git/GitHub

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd library_management
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at http://127.0.0.1:8000/

## API Testing with Postman

1. List all books:
   - GET http://127.0.0.1:8000/api/books/

2. Create a new book:
   - POST http://127.0.0.1:8000/api/books/
   - Body (JSON):
     ```json
     {
         "title": "Book Title",
         "author": "Author Name",
         "isbn": "1234567890123",
         "copies": 5
     }
     ```

## Database Management with Beekeeper Studio

1. Local Development:
   - Connect to SQLite database at `db.sqlite3`

2. Heroku:
   - Get database URL from Heroku dashboard
   - Connect using PostgreSQL connection string

## Deployment to Heroku

1. Create a Heroku account and install Heroku CLI

2. Login to Heroku:
   ```bash
   heroku login
   ```

3. Create a new Heroku app:
   ```bash
   heroku create library-management-<unique-name>
   ```

4. Add PostgreSQL addon:
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

5. Set environment variables:
   ```bash
   heroku config:set SECRET_KEY='your-secret-key'
   heroku config:set DEBUG=False
   ```

6. Deploy the application:
   ```bash
   git push heroku main
   ```

7. Run migrations:
   ```bash
   heroku run python manage.py migrate
   ```

8. Create superuser:
   ```bash
   heroku run python manage.py createsuperuser
   ```

## Testing

Run the test suite:
```bash
python manage.py test
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 