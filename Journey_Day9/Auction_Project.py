gavel=r'''
      |      |
      |      |  
      |______|
         ||
         ||
         ||
         ||
      =========
'''
print(gavel)
print("Welcome to the Auction Ladies and Gentlemen ")


Auction_Bidders={}

Auction=True

def Highest_bid(Auction):
    Max=0
    person=""
    for player in Auction:
        bidding_amount=Auction[player]
        if bidding_amount >Max:
            person=player
            Max=bidding_amount
            person=player
        else:
            continue
    print(f"The highest bid is by person {person} and bidding amount is {Max}")

while Auction:
    name=str(input("Please enter your name sir for the bid"))
    bid=int(input("Please enter your bid for the auction sir "))
    Auction_Bidders[name]=bid

    players=str(input("Are there any other bidders sir please tell Yes or No "))
    if players.lower()=="yes":
        print("\n"*100)
        continue
    else:
        Auction=False
        Highest_bid(Auction_Bidders)

print(Auction_Bidders)

print(max(Auction_Bidders,key=Auction_Bidders.get))




