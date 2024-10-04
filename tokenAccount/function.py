from random import randint
import string


def token():
    """Generates a random 8-character token containing letters and numbers.

    Returns:
        str: A random 8-character token.
    """

    # Create lists of letters and numbers
    letters = string.ascii_letters
    numbers = [str(x) for x in range(1, 10)]

    # Initialize token list
    token = []

    # Generate random characters until the token is 8 characters long
    while len(token) != 8:
        # Randomly choose between letter or number
        choice = randint(0, 1)
        if choice == 0:  # Use a number
            index = randint(0, len(numbers) - 1)
            token.append(numbers[index])
        else:  # Use a letter
            index = randint(0, len(letters) - 1)
            token.append(letters[index])

    # Join the characters into a string and return
    return "".join(token)


def protect(s):
    """Checks if the input string contains illegal characters (' or ").

    Args:
        s (str): The input string to check.

    Returns:
        str: The input string if it's valid, or an IndexError if it contains illegal characters.
    """

    if "'" in s or '"' in s:
        return IndexError("Used illegal characters, please try again")
    return s