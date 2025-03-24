import random

EASY=15
HARD=5

def set_difficulty(level):

    if level=="easy":
        return EASY
    elif level=="hard":
        return HARD

def check_both_numbers(give_number,number_to_be_guessed,user_attempts):
    attempts=user_attempts
    if give_number > number_to_be_guessed:
        print("Number guessed is too high sir ")
        return attempts-1
    elif give_number < number_to_be_guessed:
        print("Number guessed is too low sir ")
        return attempts-1


def game():
    print("Welcome to Number guessing game ")
    print("Lets see if you can correctly guess number between 1 and 100 ")

    level = str(input("Please choose easy or hard level "))
    number_to_be_guessed = random.randint(1, 100)

    user_attempts=0
    user_attempts = set_difficulty(level)
    print(f"Total attempts available are {user_attempts}")
    success=False
    while user_attempts > 0 and not success:
        give_number = int(input("Please enter your number"))
        if give_number == number_to_be_guessed:
            print(f"Congratulations sir You have guessed correct number {number_to_be_guessed} ")
            success=True
        else:
            user_attempts=check_both_numbers(give_number,number_to_be_guessed,user_attempts)
            if user_attempts==0:
                print("Sorry sir but you have lost the game sir ")
                print(f"The actual number was {number_to_be_guessed}")
            else:
                print(f"Attempts remaining {user_attempts}")

game()



