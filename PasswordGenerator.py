""""
Instructions:
Using randomized list, create a password for the user. 
The user should give how many letters should the password contain.
The user should give how many symbols would they like
The user should give how many numbers would they like in the password
"""

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["!", "#", "$", "%", "&", "*", "(", ")", "+"]

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

import random
# Easy level = generate the password in the input's order
password_easy = ""
for char in range(0, nr_letters):
    letter = random.choice(letters)
    password_easy += letter 

for sym in range (0, nr_symbols):
    symbol = random.choice(symbols)
    password_easy += symbol

for number in range(0, nr_numbers):
    num = random.choice(numbers)
    password_easy += str(num)

print(f"Easy password: {password_easy}")

# Harder level = generate the password in random order
password_hard = ""
all_lists = []
all_lists.append(letters)
for namber in numbers:
    all_lists.extend(str(namber))
all_lists.extend(symbols)

all_choice = nr_letters + nr_numbers + nr_symbols
for item in range(0, all_choice):
    pick = random.choice(all_lists)
    password_hard += str(pick)
print(f"Your hard password: {password_hard}")