# Django Contact Management System

A comprehensive contact management web application built with Django that allows users to securely store, organize, and manage their contacts with a clean, intuitive interface.

## Project Background

I developed this application to deepen my understanding of Django's capabilities and explore web development best practices. This project represents my journey into full-stack development, focusing on:

- Building secure user authentication systems
- Implementing database models with proper relationships
- Creating a responsive and user-friendly interface
- Applying CRUD operations in a real-world context
- Deploying a complete web application

## Key Features

- **Secure User Authentication**: Registration, login, and logout functionality with Django's authentication system
- **Personal Contact Management**: Each user can only access and manage their own contacts
- **Comprehensive Contact Details**: Store names, email addresses, phone numbers, profile images, and notes
- **Contact Organization**: Filter and search functionality to quickly find specific contacts
- **Responsive Design**: Mobile-friendly interface that works across all devices
- **Image Upload**: Support for contact profile pictures with proper storage handling
- **Database Integration**: SQLite backend with proper model relationships and constraints

## Technical Details

### Technologies Used

- **Backend**: Django 3.2.19, Python 3.6+
- **Database**: SQLite3 (easily upgradable to PostgreSQL for production)
- **Frontend**: HTML5, CSS3, Bootstrap 4
- **Authentication**: Django's built-in authentication system
- **Form Handling**: Django Forms with validation
- **Media Storage**: Local file system (configurable for cloud storage)

### Architecture

The application follows Django's MVT (Model-View-Template) architecture:

- **Models**: Define contact data structure with proper relationships and validation
- **Views**: Handle request processing, implement business logic, and manage authentication
- **Templates**: Present data to users with a clean, responsive interface
- **URLs**: Map requests to appropriate view functions

## Screenshots

![Contact List](path/to/screenshot1.png)
![Contact Detail](path/to/screenshot2.png)

## Installation and Setup

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Installation Steps

1. Clone the repository:
   ```
   git clone <repository-url>
   cd CONTACT_MANAGEMENT_APP_DJANGO
   ```

2. Create and activate a virtual environment:
   ```
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (admin):
   ```
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

7. Access the application at http://127.0.0.1:8000

### Alternative Setup (Automated)

Run the appropriate setup script for your platform:

- Windows: `setup.bat`
- macOS/Linux: `setup.sh`

## What I Learned

This project significantly improved my understanding of:

- Django's model-view-template architecture
- User authentication and security best practices
- Form validation and handling
- File uploads and media management
- Database design and relationships
- Bootstrap integration for responsive design
- Django admin customization

## Future Enhancements

I plan to extend this project with:

- Contact grouping and categorization
- Birthday reminders and notifications
- Import/export functionality for contacts
- Contact sharing between users
- Dark mode theme option
- Enhanced mobile experience with PWA features
- Cloud storage integration for contact images

## Usage Guide

1. Register for an account or log in
2. Add contacts through the "Add Contact" button
3. View your contacts on the home page
4. Search for specific contacts using the search bar
5. Click on a contact to view details
6. Edit or delete contacts from their detail page




