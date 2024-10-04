import sqlite3
from function import token, protect

# Connect to the database
connection = sqlite3.connect("accounts.db")
cursor = connection.cursor()

# Initialize password variable
password = None

# Main loop for selecting new or old account
while True:
    # Prompt user for input
    inpt = input("New or Old account (N/O): ").lower()

    # Handle new account creation
    if inpt == "n":
        # Loop for password input validation
        while True:
            # Prompt user for password input choice
            q = input("Do you want to enter a password or generate one? (E/G): ").lower()

            # Handle entering a password
            if q == "e":
                password = input("Enter a new password: ")
                break

            # Handle generating a password
            elif q == "g":
                password = token()
                break

            # Handle invalid input
            else:
                print("Invalid input. Please enter 'E' for entering a password or 'G' for generating one.")

        # Generate a username and insert account into database
        user = token()

        # Check if the username is unique
        while True:
            result = cursor.execute("SELECT * FROM accounts WHERE token = ?", (user,)).fetchall()
            if len(result) == 0:
                break
            else:
                print("Username already exists. Please try another username.")
                user = token()

        id = len(cursor.execute("SELECT * FROM accounts").fetchall()) + 1
        cursor.execute("INSERT INTO accounts (id, token, password) VALUES (?, ?, ?)", (id, user, password))
        connection.commit()

        # Print success message
        print(f"\nAccount created successfully!\nYour username is: {user}\nYour password is: {password}")
        print("Remember to save your username and password for future logins.")
        break

    # Handle existing account login
    elif inpt == "o":
        # Prompt user for username and password
        usr = protect(input("Enter your username: "))
        password = protect(input("Enter your password: "))

        # Check if login credentials are valid
        try:
            result = cursor.execute("SELECT * FROM accounts WHERE token = ? AND password = ?", (usr, password)).fetchall()
            if len(result) > 0:
                print("\nLogin successful to " + usr)
                break
            else:
                print("\nLogin failed, check username and password")
                break
        except sqlite3.InterfaceError as e:
            print(f"There was a problem with the database: {e}")  # More informative message
        except Exception as e:
            print(f"An unexpected error occurred: {e}")  # Generic fallback message

    # Handle invalid input
    else:
        print("Invalid input, please try again entering 'N' for new account or 'O' for existing account")