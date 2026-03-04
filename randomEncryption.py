#randomEncryption

import random
import encryption

def generateRandomMapping():
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")
    shuffled = alphabet.copy()
    random.shuffle(shuffled)
    mapping = dict(zip(alphabet, shuffled))
    return mapping

def encrypt(text, mapping):
    return ''.join(mapping.get(c, c) for c in text)

def decrypt(text, mapping):
    reverse_mapping = {v: k for k, v in mapping.items()}
    return ''.join(reverse_mapping.get(c, c) for c in text)

#Main Program

previousPassword=str(input("Do you have a password to encrypt? (y/n): "))

if(previousPassword.lower()=="n"):
    import passwordGenerator 
    passwordGenerator
    password=passwordGenerator.generate_password(combined,length)

if(previousPassword.lower()=="y"):

    password=input("Enter the password you want to encrypt: ")

    cypherChoice=str(input("Do you want to encrypt the password using Ceaser Cypher? (y/n): "))

    if(cypherChoice.lower()=="y"):
        shift=int(input("Enter the shift number for Ceaser Cypher: "))
        encryptionPassword=encryption.caesarCypher(password,shift)
        print(f"Encrypted Password: {encryptionPassword}")

    randomChoice=str(input("Do you want to encrypt the password using Random Encryption? (y/n): "))

    if (randomChoice.lower()=="y"):
        mapping = generateRandomMapping()

        encryptionRandomPassword=encrypt(password, mapping)

        print(f"Encrypted Password using Random Encryption: {encryptionRandomPassword}")
