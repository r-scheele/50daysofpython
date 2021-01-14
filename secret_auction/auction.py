import os
from arts import logo

print(logo)

bidders = {}
bidder_name = input("What's your name? ")
bidding_amount = int(input("What's your bid? "))

def auction(bidder, bid_price):
    bidders[bidder] = bid_price

auction(bidder_name, bidding_amount)

replay = True
while replay:
    another = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if another == 'yes':
        os.system('clear')
        print(logo)
        bidder_name = input("What's your name? ")
        bidding_amount = int(input("What's your bid? "))
        auction(bidder_name, bidding_amount)

    else:
        os.system('clear')
        print(logo)
        replay = False

highest_bid = 0
for bidder in bidders:
    price = bidders[bidder]
    if price > highest_bid:
        highest_bid = price
        name = bidder
print(f"The winner is {name} with a bid of {highest_bid}")