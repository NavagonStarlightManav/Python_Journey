import random
import add


def my_function():
    for i in range(1,21):
        if i==20:
            print("You got it")
my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# 2. When is the function meant to print "You got it"?
# 3. What are your assumptions about the value of i?


dice_images=["1","2","3","4","5","6"]
dice_num=random.randint(0,5)
# Now here there will be List index out of bounds error so we changed to 5
print(dice_images[dice_num])


year=int(input("What's your year of birth? "))

if year>1980 and year<1994:
    print("You are millenmial ")
elif year>=1994:
    print("Your are Gen Z ")


try:
    age=int(input("How old are you? "))
except ValueError:
    print("SIr you have typed an invalid number , please again try with another numerical option ")
    age = int(input("How old are you? "))
if age>18:
    print(f"you can drive at age {age}")


pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))

total_words = pages * word_per_page

print(f"pages = {pages}")
print(f"words_per_page = {word_per_page}")
print(total_words)

def mutate(a_list):
    b_list=[]
    new_item=0
    for item in a_list:
        new_item=item*2
        new_item+=random.randint(1,2)
        new_item=add.adding(new_item,item)
        b_list.append(new_item)
    print(b_list)

# put breakpoint on that line on which you want to see variables updating  every time
# step into code will go through all modules used in the code
# step into my code will ignore the import modules while running
# in console we can see final output
# in variables and threads we see variables updating side by side
# breakpointing a line means that code will pause execution at that line for a moment to show us current situation


mutate([1,2,3,5,8,13])

