# Function to encrypt text using Caesar Cipher
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_value = shift % 26  # Shift wraps around for alphabet
            ascii_offset = 65 if char.isupper() else 97
            new_char = chr((ord(char) - ascii_offset + shift_value) % 26 + ascii_offset)
            encrypted_text += new_char
        else:
            encrypted_text += char  # Non-alphabetical characters remain unchanged
    return encrypted_text

# Function to decrypt text using Caesar Cipher
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # Decrypting is the same as encrypting with negative shift

# Main function to handle user input and perform encryption/decryption
def main():
    print("Caesar Cipher Program")
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    action = input("Do you want to (e)ncrypt or (d)ecrypt the message? ").lower()
    if action == 'e':
        encrypted_message = caesar_encrypt(message, shift)
        print("Encrypted Message:", encrypted_message)
    elif action == 'd':
        decrypted_message = caesar_decrypt(message, shift)
        print("Decrypted Message:", decrypted_message)
    else:
        print("Invalid option. Please enter 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
