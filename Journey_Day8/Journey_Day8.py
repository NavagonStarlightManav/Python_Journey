def Greet():
    print("How are you angela ")
    print("How do you do Angela")
    print("Isn't the weather nice")

Greet()

def greet_with_name(name):
    print(f"hello {name}")
    print(f"how do you do {name}")

greet_with_name("Angela")

def life_in_weeks(age):
    print(f"You have {(90-age)*52} weeks left")

life_in_weeks(54)

def greet_with(name,location):
        print(f"Hello {name}" )
        print(f"What is it like in {location}")

greet_with("jack baurer","nowhere")

greet_with(location="chandigarh",name="Angela") # These are called the keyword arguments


def calculate_love_score(word1, word2):
    first ="True"
    second ="Love"
    word_join = (word1 + word2).lower()

    count1 = 0
    count2 = 0
    j=0
    k=0

    while j!=len(first):
        temp=first[j].lower()
        for letter in word_join:
            if letter==temp:
                count1 += 1
            else:
                continue
        j+=1

    while k!=len(second):
        temp2=second[k].lower()
        for letter in word_join:
            if letter==temp2:
                count2 += 1
            else:
                continue
        k+=1

    love_score = int(str(count1) + str(count2))

    print(f"The Love score is {love_score}")

calculate_love_score("Manav","Navreet")