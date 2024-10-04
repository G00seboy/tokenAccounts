# tokenAccounts
Random project

Project Description: User Authentication and Account Management System

Purpose:

This Python project provides a user authentication and account management system. It allows users to create new accounts, log in to existing ones, and manage their personal information.

Features:

    User Registration: Users can create new accounts. The system generates a unique Username and password for each account.
    User Login: Users can log in to their existing accounts by entering their username and password.
    Password Management: Users can choose to enter their own passwords or have them generated randomly.
    Input Validation: The system validates user input to prevent illegal characters and potential security vulnerabilities.
    Database Integration: The project utilizes a SQLite database to store user information, including their ID, username, and password.
    Error Handling: The system includes error handling mechanisms to provide informative messages to the user in case of unexpected errors or database issues.

Technologies:

    Python
    SQLite database
    random and string modules for password generation and validation

Usage:

    Create a new account:
        Run the Python script.
        Choose "N" for New account.
        Enter a password or generate one randomly.
        The system will create a new account and display the generated username and password.
    Log in to an existing account:
        Run the Python script.
        Choose "O" for Old account.
        Enter your username and password.
        If the credentials are correct, you will be logged in successfully.
