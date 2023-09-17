import random
import string
from builtins import input, range, int, print, ValueError


def generate_password(length):
    # Define character sets for different complexity levels
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Combine character sets based on user preferences
    characters = lower_case + upper_case + digits  # Default complexity
    complexity = input("Enter complexity level (l, m, h for low, medium, high): ").lower()
    if complexity == 'm':
        characters += special_chars
    elif complexity == 'h':
        characters += upper_case + digits + special_chars

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length should be a positive integer.")
            return
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")


if __name__ == "__main__":
    main()
