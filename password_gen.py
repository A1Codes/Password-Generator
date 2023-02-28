import random
import string

print("Password Generator")

letters = list(string.ascii_letters)
symbols = list(string.punctuation)
numbers = list(string.digits)

nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like in your password? "))
nr_numbers = int(input("How many numbers would you like in your password? "))

password = []

for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

random.shuffle(password)
new = ''.join(password)

print(f"Your generated password is: {new}")