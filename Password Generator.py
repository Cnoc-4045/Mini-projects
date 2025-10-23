#Password Generator
import random
import math

alphabetUpper=[""]*26
alphabet=[""]*26
number=[""]*10
symbol=["!","@","#","$","%","^","&","*","(",")"]

for i in range(26):
    alphabet[i]=chr(97+i)

for i in range(10):
    number[i]=str(i)

for i in range(26):
    alphabetUpper[i]=chr(65+i)

combined=number+alphabet+symbol+alphabetUpper

length=int(input("Enter the length of password: "))

password_chars = [
    random.choice(alphabetUpper),
    random.choice(alphabet),
    random.choice(number),
    random.choice(symbol)
]

def generate_password(combined,length):
    password=""
    password+="".join(password_chars)
    for i in range(length-4):
        password+=random.choice(combined)
    return password

password=generate_password(combined,length)

print(f"Generated Password: {password}")