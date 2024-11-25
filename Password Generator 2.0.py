import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1','2', '3', '4', '5','6', '7', '8','9']
symbols = ['!', '#', '$', '%', '&','(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your passowrd?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

password_list = []

for char in range(0, nr_letters): #This generates the number of letters in the list
    password_list.append(random.choice(letters)) #This generates random letters

for char in range(0, nr_symbols): #This generates the number of symbols in the list
    password_list.append(random.choice(symbols)) #This generates random symbols

for char in range(0, nr_numbers): #This generates the number of numbers in the list
    password_list.append(random.choice(numbers)) #This generates random numbers

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
