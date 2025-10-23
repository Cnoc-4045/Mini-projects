#Encryption

def caesarCypher(text, shift):
        encrypted = ""

        for char in text:
            if char.isalpha():  # only shift letters
                # Handle uppercase and lowercase separately
                start = ord('A') if char.isupper() else ord('a')
                # Shift the letter and wrap around using modulo 26
                encrypted += chr((ord(char) - start + shift) % 26 + start)
            else:
                # Keep non-letters as-is
                encrypted += char

        return encrypted

if input("Do you already have a password to encrypt? (y/n): ")=="y":
    password=str(input("Enter the password to encrypt: "))

    shift=int(input("Enter the shift number for Ceaser Cypher: "))

    encryption=caesarCypher(password, shift)

    print(f"Encrypted Password: {encryption}")