############### Blackjack Project #####################
import random
from art import logo


# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
def black_jack():
    end_of_game = False
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    answer = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
    if answer == 'n':
        end_of_game = True
    computer_card = []
    my_card = []

    for _ in range(2):
        computer_card.append(random.choice(cards))
        my_card.append(random.choice(cards))
    while not end_of_game:
        print(logo)
        print(f"Your cards: {my_card}, current score: {sum(my_card)}")
        print(f"Computer's first card: {computer_card[0]}")
        if sum(my_card) == 21 and len(my_card) == 2:
            print(f" Your final hand:{my_card}, final score: {sum(my_card)}")
            print(f" Computer's final hand: {computer_card}")
            print("You win.😃")
            black_jack()
            return
        repeat_answer = input("Type 'y' to get another card, type 'n' to pass: ")
        if repeat_answer == 'y':
            computer_card.append(random.choice(cards))
            my_card.append(random.choice(cards))
            if sum(my_card) > 21:
                if 11 in my_card:
                    my_card.remove(11)
                    my_card.append(1)
                    continue
                print(f" Your final hand:{my_card}, final score: {sum(my_card)}")
                print(f" Computer's final hand: {computer_card}")
                print("You went over. You lose.😭")
                black_jack()
                return
        else:
            while sum(computer_card) < 17:
                computer_card.append(random.choice(cards))
            if sum(my_card) <= 21 and sum(computer_card) <= 21:
                a = 21 - sum(my_card)
                b = 21 - sum(computer_card)
                if a < b:
                    print(f" Your final hand:{my_card}, final score: {sum(my_card)}")
                    print(f" Computer's final hand: {computer_card}")
                    print("You win.😃")
                elif a > b:
                    print(f" Your final hand:{my_card}, final score: {sum(my_card)}")
                    print(f" Computer's final hand: {computer_card}")
                    print("You lose.😭")
                else:
                    print(f" Your final hand:{my_card}, final score: {sum(my_card)}")
                    print(f" Computer's final hand: {computer_card}")
                    print("You draw.😭")
            elif sum(my_card) > 21:
                if 11 in my_card:
                    my_card.remove(11)
                    my_card.append(1)
                    continue
                print(f" Your final hand:{my_card}, final score: {sum(my_card)}")
                print(f" Computer's final hand: {computer_card}")
                print("You went over. You lose.😭")
            elif sum(computer_card) > 21:
                if 11 in my_card:
                    my_card.remove(11)
                    my_card.append(1)
                    continue
                print(f" Your final hand:{my_card}, final score: {sum(my_card)}")
                print(f" Computer's final hand: {computer_card}")
                print("You win.😃")
            black_jack()
            return


black_jack()

