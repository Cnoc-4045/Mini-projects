#Encryption

previousPassword=str(input("Do you have a password to encrypt? (y/n): "))

def caesarCypher(text, shift):
    ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    lookup = {c: i for i, c in enumerate(ALPHABET)}
    encrypted = []

    for char in text:
        if char in lookup:
            idx = (lookup[char] + shift) % len(ALPHABET)
            encrypted.append(ALPHABET[idx])
        else:
            encrypted.append(char)

    return ''.join(encrypted)

def caesar_decipher(text, shift):
    return caesarCypher(text, -shift)


if previousPassword.lower()=="y":
    password=str(input("Enter the password to encrypt: "))

    shift=int(input("Enter the shift number for Ceaser Cypher: "))

    encryption=caesarCypher(password, shift)

    print(f"Encrypted Password: {encryption}")