def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += shifted_char
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text += shifted_char
        else:
            # Non-alphabetic characters remain unchanged
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Choose an option (E for encryption, D for decryption): ").upper()
    if choice == 'E':
        plaintext = input("Enter the text to encrypt: ")
        shift_value = int(input("Enter the shift value (positive integer): "))
        encrypted_result = encrypt(plaintext, shift_value)
        print(f"Encrypted Text: {encrypted_result}")
    elif choice == 'D':
        encrypted_text = input("Enter the text to decrypt: ")
        shift_value = int(input("Enter the shift value (positive integer): "))
        decrypted_result = decrypt(encrypted_text, shift_value)
        print(f"Decrypted Text: {decrypted_result}")
    else:
        print("Invalid choice. Please select E or D.")

if __name__ == "__main__":
    main()
