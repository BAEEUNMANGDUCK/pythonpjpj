# Hangman  만들기 프로젝트

import random
import hangman_words as hw
from hangman_art import stages, logo


#Step 1, #Step 2, #Step3
print(logo)

word_list = hw.word_list

# TODO 7: Create a variable called 'lives'
lives = 6

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(f"chosen word is {chosen_word}")


#TODO-4: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []

for _ in range(len(chosen_word)):
    display.append("_")


print(" ".join(display))

print(stages[6])

end_of_game = False


while not end_of_game:
    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

    guess = input("Guess a word: ").lower()
    # print(guess)


    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

    # for alpha in chosen_word:
    #     if guess == alpha:
    #         print("Right")
    #     else:
    #         print("Wrong")


    #TODO-5: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].


    #TODO 8: If guess is not a letter in the chosen_word: then reduce 'lives' by 1

    if guess not in chosen_word:
        print(f" you guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(stages[lives])
    else:
        if guess in display:
            print(f"You've already guessed {guess}")
        for idx in range(len(chosen_word)):
            if chosen_word[idx] == guess:
                display[idx] = guess
        print(stages[lives])


    #TODO-6: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
    print(" ".join(display))

    if "_" not in display:
        end_of_game = True
        print("You win.")

    if lives < 1:
        end_of_game = True
        print("You lose")



