# Password Manager

A Python-based password manager with GUI that allows users to generate, store, and retrieve secure passwords.

## Features

- Generate random passwords with various strength levels:
  - Low: lowercase letters only
  - Medium: uppercase and lowercase letters
  - Strong: letters, numbers, and special characters
- Customizable password length (8-32 characters)
- Copy passwords to clipboard
- Save passwords along with username and website information
- View all saved passwords
- Local storage in a text file

## Screenshots

![Password Manager Screenshot](screenshots/password_manager.png)

## How to Use

1. Install the required dependencies:
   ```
   pip install pyperclip
   ```

2. Run the application:
   ```
   python password.py
   ```

3. To generate a password:
   - Select desired strength (Low, Medium, Strong)
   - Choose password length from dropdown
   - Click "Generate"
   
4. To save a password:
   - Enter username and website
   - Generate or enter a password
   - Click "Save"
   
5. To view all saved passwords:
   - Click "Show all passwords"
   - Passwords will be displayed in the console

## Security Note

This application stores passwords in plain text in a local file (info.txt). For educational purposes only - not recommended for storing actual sensitive passwords.

## Requirements

- Python 3.x
- Tkinter (usually comes with Python)
- pyperclip

## License

This project is part of the Awesome Python Projects collection and is available under the MIT License. 