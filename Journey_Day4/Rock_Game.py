import random

print("Welcome to the rock paper scissor paper game. Please choose 0 for rock , 1 for scissor , 2 for paper ")
user_choice=int(input("Please tell your choice sir "))
computer_choice=random.randint(0,2)

rock = '''     
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
 '''
scissors = '''     
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
paper  = '''      
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
 '''

choices=[rock,scissors,paper]
print(f"user choice is \n{choices[user_choice]}")
print(f"computer choice is \n{choices[computer_choice]}")

if user_choice==computer_choice:
    print("Its draw sir ")
if user_choice==0:
    if computer_choice!=2:
        print("You win sir against our mighty computer")
    else:
        print("Sorry sir computer wins  Please try again ")

if user_choice==1:
    if computer_choice!=0:
        print("You win sir ")
    else:
        print("Sorry sir computer wins please try again ")

if user_choice==2:
    if computer_choice!=1:
        print("You win sir ")
    else:
        print("Sorry sir Computer wins please try agains")