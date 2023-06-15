from art import logo

print(logo)

print("Welcome to the secret auction program.")
end_of_bid = False
bid_dict = {}

def find_highest_bidder(bidding_record):
    max_bidder = {"bidder_name": "", "bid_money": 0,}

    for bidder in bidding_record:
        if money < bid_dict[bidder]:
            max_bidder["bidder_name"] = bidder
            max_bidder["bid_money"] = bid_dict[bidder]
    return max_bidder

while not end_of_bid:
    bidder = input("What is your name?: ")
    money = int(input("What's your bid?: $"))
    bid_dict[bidder] = money
    print(bid_dict)
    yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if yes_or_no == 'yes':
        continue
    else:
        end_of_bid = True
        highest = find_highest_bidder(bid_dict)
        print(f"The winner is {highest['bidder_name']} with a bid of ${highest['bid_money']}")


