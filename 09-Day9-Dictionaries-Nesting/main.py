import art
print(art.logo)

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
while True:
    name = input("What is your name?\n")
    price = int(input("What's your bid? \n$"))
    bids[name] = price

    while True:
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").strip().lower()
        if should_continue == 'yes':
            print("\n" * 20)
            break
        elif should_continue == 'no':
            break
        print("Invalid input. Please type 'yes' or 'no'.")
    if should_continue == 'no':
        print(bids)
        find_highest_bidder(bids)
        break
