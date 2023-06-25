# import art, game_data, and random
# from replit import clear
from art import logo, vs
import game_data
import random

# define score as constant variable
SCORE = 0


# Define function for comparing followers
def compare_follower(a_cel, b_cel):
    if a_cel['follower_count'] > b_cel['follower_count']:
        return 'a'
    else:
        return 'b'


def higher_lower_game():
    global SCORE
    end_of_game = False
    a, b = random.choices(game_data.data, k=2)
    while not end_of_game:
        #  clear()
        print(logo)
        # choice two celebrities by using random module
        if SCORE != 0:
            print(f"You're right! Current score: {SCORE}")
        print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
        print(vs)
        print(f"Compare B: {b['name']}, {b['description']}, from {b['country']}")

        print(f"psst a_count: {a['follower_count']}, b_count:{b['follower_count']}")
        winner = compare_follower(a_cel=a, b_cel=b)
        print(winner)

        # answer the question
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        # pass or fail
        if winner == answer:
            SCORE += 1
        else:
            # clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {SCORE}")
            end_of_game = True
        # b의 데이터가 a로 가고, b는 새로 데이터를 뽑음, 그런데 새로 뽑은 b의 데이터가 a랑 같을 수도 있으니까 while문에 넣어서 둘이 같은 경우가 나오면 다른 경우가 나올때 까지 비교함.
        a = b
        b = random.choice(game_data.data)
        while a == b:
            b = random.choice(game_data.data)


higher_lower_game()
