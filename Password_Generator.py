import random
import string

def generate_password(length, num_symbols, num_digits):
    # Define the characters to use in the password
    letters = string.ascii_letters
    symbols = string.punctuation
    digits = string.digits

    # Ensure the requested length is sufficient for symbols and digits
    total_length = length + num_symbols + num_digits
    if total_length < 8:
        print("Password length must be at least 8 characters.")
        return None

    # Generate the password
    password = ''.join(random.choice(letters) for _ in range(length))
    password += ''.join(random.choice(symbols) for _ in range(num_symbols))
    password += ''.join(random.choice(digits) for _ in range(num_digits))
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

try:
    desired_length = int(input("Enter how many letters you want in your password "))
    num_symbols = int(input("Enter how many number of symbols you want in your password  (e.g., !@#$%^&*): "))
    num_digits = int(input("Enter how many number of digits you want in your password  (0-9): "))

    generated_password = generate_password(desired_length, num_symbols, num_digits)
    if generated_password:
        print(f"Generated Password--> {generated_password}")
except ValueError:
    print("Invalid input. Please enter valid positive integers.")
