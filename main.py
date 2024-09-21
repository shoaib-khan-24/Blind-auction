import art
print(art.logo)

def find_highest_bidder( dictionary_of_bidder):
    max_bid = 0
    winner_name = ""
    for bidder in dictionary_of_bidder:
        if dictionary_of_bidder[bidder] > max_bid:
            max_bid = dictionary_of_bidder[bidder]
            winner_name = bidder
    print(f"Winner is {winner_name} with bid ${max_bid}")

print("*** WELCOME TO THE BLIND AUCTION ***\n\n")
auction_over = False
auction_information = {}

while not auction_over:
    name = input("Enter the name of bidder:  ")
    bid = int(input("Enter the bid:  $"))
    auction_information[name] = bid

    choice = input("More bidders? Type 'yes' or 'no'.\n")
    if choice == "no":
        auction_over = True
        print("\n"*20)
        find_highest_bidder(auction_information)
    elif choice == "yes":
        print("\n"*20)
    else:
        print("Wrong choice. Get out of the auction.")
        auction_over = True
