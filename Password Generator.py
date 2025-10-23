#Password Generator
import random
import math

alphabet=[""]*26
number=[""]*10
symbol=["!","@","#","$","%","^","&","*","(",")"]

for i in range(26):
    alphabet[i]=chr(97+i)

for i in range(10):
    number[i]=str(i)

combined=number+alphabet+symbol

def generate_password(combined):
    password=""
    length=int(input("Enter the length of password: "))
    for i in range(length):
        password+=random.choice(combined)
    return password

password=generate_password(combined)

print(f"Generated Password: {password}")