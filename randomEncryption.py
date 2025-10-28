#randomEncryption

import random

def generateRandomMapping():
    # Original alphabet: lowercase + uppercase
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")
    shuffled = alphabet.copy()
    random.shuffle(shuffled)
    # Mapping: original → substitute
    mapping = dict(zip(alphabet, shuffled))
    return mapping

def encrypt(text, mapping):
    # Replace each character with its substitute
    return ''.join(mapping.get(c, c) for c in text)

def decrypt(text, mapping):
    # Reverse mapping: substitute → original
    reverse_mapping = {v: k for k, v in mapping.items()}
    return ''.join(reverse_mapping.get(c, c) for c in text)

previousPassword=str(input("Do you have a password to encrypt? (y/n): "))

if(previousPassword.lower()=="y"):
    password=str(input("Enter the password to encrypt: "))

    mapping = generateRandomMapping()

    encryption = encrypt(password, mapping)

    print(f"Encrypted Password: {encryption}")

    # For demonstration, decrypting back to original
    decrypted = decrypt(encryption, mapping)
    print(f"Decrypted Password: {decrypted}")