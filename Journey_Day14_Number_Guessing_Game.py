import random

vs_symbol = """
██    ██  ████████      ███████ 
 ██  ██      ██        ██       
  ████       ██        █████    
   ██        ██        ██       
   ██        ██        ███████  
"""

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 175,
        'description': 'Model and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 200,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 170,
        'description': 'Singer-songwriter',
        'country': 'United States'
    },
    {
        'name': 'Elon Musk',
        'follower_count': 160,
        'description': 'Entrepreneur and CEO of Tesla & SpaceX',
        'country': 'United States'
    },
    {
        'name': 'YouTube',
        'follower_count': 160,
        'description': 'Video sharing platform',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 190,
        'description': 'Singer and actress',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 165,
        'description': 'TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'NASA',
        'follower_count': 110,
        'description': 'Space agency',
        'country': 'United States'
    },
    {
        'name': 'Neymar Jr.',
        'follower_count': 150,
        'description': 'Footballer',
        'country': 'Brazil'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 120,
        'description': 'Singer-songwriter',
        'country': 'United States'
    },
    {
        'name': 'Netflix',
        'follower_count': 90,
        'description': 'Streaming platform',
        'country': 'United States'
    }
]
def comparison(Milennial_1,Milennial_2):
    if Milennial_1['follower_count']<Milennial_2['follower_count']:
        return "B"
    else:
        return "A"


user_wins=True
count=0

Milennial_1 = random.choice(data)
Milennial_2 = random.choice(data)
if Milennial_1==Milennial_2:
    Milennial_2=random.choice(data)


while user_wins :

    print(f"First one is {Milennial_1['name']} being {Milennial_1['description']} from {Milennial_1['description']}")
    print(vs_symbol)
    print(f"second one is {Milennial_2['name']} being {Milennial_2['description']} from {Milennial_2['description']}")

    user_choice=str(input("Please choose A or B depending upon whose followers are more "))


    True_guess=comparison(Milennial_1, Milennial_2)
    if True_guess.lower()==user_choice.lower():
        count += 1
        print(f"Well You guessed correctly sir  and current score is {count}")
        if user_choice.lower()=="a":
            Milennial_2=random.choice(data)
        elif user_choice.lower()=="b":
            Milennial_1=Milennial_2
            Milennial_2=random.choice(data)

    else:
        user_wins=False
        print(f"Sorry sir you have lost the game with current score of {count}")






