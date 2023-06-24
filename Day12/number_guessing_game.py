from art import logo
import random

LIVES = 0


def guess_the_number(answer, guess):
    if answer > guess:
        print("Too Low.")
        return LIVES - 1
    elif answer < guess:
        print("Too high.")
        return LIVES - 1
    else:
        print(f"You got it! The answer was {answer}")
        return 1000


def number_guess_game():
    # 원래는 함수 내부에 있는 LIVES 값과 함수 외부에 있는 LIVES 값은 별개이지만 global 예약어를 사용해서 외부에 LIVES = 0 값이 10 또는 5가 될 수 있다. 따라서
    # guess_the_number 함수를 사용할 때에도 10 또는 5라는 LIVES 값이 연산되어 줄어들고 해당 값이 반환되어 다시 LIVES 값에 대입이 됨
    global LIVES
    print(logo)
    answer = random.randint(1, 100)
    end_of_game = False
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    print(f"Pssst, the correct answer is {answer}")
    if difficulty == 'easy':
        LIVES = 10
    else:
        LIVES = 5

    while not end_of_game:
        print(f"You have {LIVES} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        LIVES = guess_the_number(answer, guess)
        if LIVES == 1000:
            end_of_game = True
        elif LIVES == 0:
            print("You've run out of guesses, you lose")
            end_of_game = True
        else:
            print("Guess again.")


number_guess_game()
