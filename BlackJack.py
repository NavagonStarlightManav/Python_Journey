import random

from Journey_Day5 import number

blackjack_art = """
██████╗ ██╗      █████╗  ██████╗██╗  ██╗      ██████╗  █████╗ ███╗   ███╗███████╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝      ██╔══██╗██╔══██╗████╗ ████║██╔════╝
██████╔╝██║     ███████║██║     █████╔╝ █████╗██████╔╝███████║██╔████╔██║█████╗  
██╔═══╝ ██║     ██╔══██║██║     ██╔═██╗ ╚════╝██╔═══╝ ██╔══██║██║╚██╔╝██║██╔══╝  
██║     ███████╗██║  ██║╚██████╗██║  ██╗      ██║     ██║  ██║██║ ╚═╝ ██║███████╗
╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝      ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

♠ ♡ ♣ ♢ 𝄞 𝄞 𝄞 𝄞 𝄞 WELCOME TO THE BLACKJACK CASINO! 𝄞 𝄞 𝄞 𝄞 𝄞 ♠ ♡ ♣ ♢
═══════════════════════════════════════════════════════════════════════════
                            ★ ★ ★ TABLE ★ ★ ★
┌──────────────────────────────────────┐
│  🎩 Dealer Hand: [♠?] [♦K]           │
│  🃏 Player Hand: [♥10] [♣9]           │
│                                        
│  🎲 [H] Hit     💰 [D] Double         │
│  🛑 [S] Stand   🚪 [Q] Quit           │
└──────────────────────────────────────┘
═══════════════════════════════════════════════════════════════════════════
"""
welcome=blackjack_art+"\n"+"Welcome to The house baby "

cards = {
    'Ace': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
}

def calculate_score(User_cards):
    """ Take the list and returns its score """
    if sum(User_cards) == 21 and len(User_cards) == 2:
        return 0
    elif 11 in User_cards and sum(User_cards)>21:
        User_cards.remove(11)
        User_cards.append(1)
        return sum(User_cards)
    else:
        return sum(User_cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 😐"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😆"
    elif u_score > c_score:
        return "You win 🙂"
    else:
        return "You Lose 😱"

game=True
def blackjack():
    print(welcome)
    computer_score = -1
    user_score = -1

    Dealers_card = []
    User_cards = []

    Dealers_card.append(cards[random.choice(list(cards.keys()))])
    Dealers_card.append(cards[random.choice(list(cards.keys()))])

    User_cards.append(cards[random.choice(list(cards.keys()))])
    User_cards.append(cards[random.choice(list(cards.keys()))])

    print(f"First card of Dealer is {Dealers_card[0]}")

    game_run = True

    while game_run:
        print(f"Your cards are sir {User_cards}")
        user_score = calculate_score(User_cards)
        computer_score = calculate_score(Dealers_card)
        print(f"user score is {user_score} ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            print("Sorry sir you have lost ")
        else:
            pass_choice = str(input("Sir please press'bet' for continue and 'take' for another card"))
            if pass_choice.lower() == "bet":
                game_run = False

            elif pass_choice.lower() == "take":
                (
                    User_cards.append(cards[random.choice(list(cards.keys()))]))

    while computer_score != 0 and computer_score < 17:
        Dealers_card.append(cards[random.choice(list(cards.keys()))])
        computer_score = calculate_score(Dealers_card)

    print(f"so finally user cards are {User_cards} and computer cards are {Dealers_card}")
    print(compare(user_score, computer_score))


    new_game=str(input("sir wanna have another game? yes or no "))
    if new_game=="yes":
        print("\n"*100)
        blackjack()
    else:
        game=False



blackjack()


















