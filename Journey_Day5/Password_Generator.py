import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]

collection=[letters,numbers,symbols]

password=[]

print("Welcome to the PyPassword Generator")
nr_letters=int(input("How many letters would you like in your password?\n"))
nr_symbols=int(input("How many symbols would you like?\n"))
nr_numbers=int(input("How many numbers would you like?\n"))

current_length=0
max_length=nr_numbers+nr_letters+nr_symbols
letter_count=0
symbol_count=0
number_count=0

while current_length!=max_length:
    type=random.choice(collection)

    if type==letters:
        if letter_count<nr_letters:
            password.extend(random.choice(symbols))
            letter_count+=1
            current_length += 1
    elif type==symbols:
        if symbol_count<=nr_symbols:
            password.extend(random.choice(symbols))
            symbol_count+=1
            current_length += 1
    elif type==numbers:
        if number_count<nr_numbers:
            password.extend(random.choice(numbers))
            number_count+=1
            current_length += 1
    else:
        continue
print(password)

# random.shuffle function can  also be used
