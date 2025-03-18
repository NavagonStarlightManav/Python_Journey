stages = [
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / 
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |    
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|
      |    
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |    |
      |    
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |    
      |    
      |
    --------
    """,
    """
      ------
      |    |
      |    
      |    
      |    
      |
    --------
    """
]

hangman_logo = r'''
  _                                             
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___                      
'''
print(hangman_logo)


import random

words=["Vaishnavi","Nancy","Monica Chandler","Phoebe"]

#looping Through list
def if_belongs_to_word(word,guessed_letter,current_word):
   found=False
   updated_word=[]

   length=len(word)

   for i in range(0,length):
        if word[i]==guessed_letter:
            current_word[i]=guessed_letter
            updated_word=current_word
            found=True
        else:
            continue

   return found

blank = "_"

def no_blanks(word):
    return blank not in word #Directly traverse for checking same thing with everything in string or use manual function at last

print("Welcome to the Hangman Game, sir! It's gonna be highly fun")

Word_to_be_guessed = random.choice(words).lower()

length_of_words = len(Word_to_be_guessed)

current_word = [blank] * length_of_words # created empty list at same time and assigned values particular number of times or look at alterantives at last

life = 6

while not no_blanks(current_word) and life > 0:
    print(f"Lives remaining: {life}")
    letter_guessed = str(input("Please enter a letter").lower())

    if if_belongs_to_word(Word_to_be_guessed,letter_guessed,current_word):
        print(f"You are good to go {current_word}")
        print(stages[life])
    else:
        print(f"Incorrect guess Think again with word {current_word}")
        life=life-1
        print(stages[life])
        if letter_guessed in current_word:
            print("Sir you already choose this letter")

if no_blanks(current_word):
    print("\n Congratulations! You guessed the word:", Word_to_be_guessed)
else:
    print("\n You lost! The word was:", Word_to_be_guessed)

# def no_blanks(word):
#     for char in word:
#         if char == blank:
#             return False
#     return True

# current_word=""
# for place in range(1,length_of_words):        # just for initial printing
#      current_word+="_"

# for letter in Word_to_be_guessed:
#     if letter==letter_guessed:
#         current_word=letter
#     else:
#         current_word="_"

# very important that take care of lists and strings