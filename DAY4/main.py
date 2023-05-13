import random
import my_module  

random_integer = random.randint(1,10)
print(random_integer)
print(my_module.pi)

# random_float = random.random()
# print(random_float)

#random decimal number
random_0_to_5 = random.random() * 5
print(random_0_to_5)

#Example 1

heads_or_tails = random.randint(0,1)

if heads_or_tails == 0:
    print("Tails")
else:
    print("Heads")

# Python List 

states_of_america = ["Delaware", "Pennsylvania", "New York", "Texas"]

states_of_america[3] = "texxxas"

states_of_america.append("Hawaii")

states_of_america.extend(["Helloland","Byeland"])

print(states_of_america)



names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ") #인자를 기준으로 나눠서 리스트의 요소로 만듬


num_names = len(names)
random_name = names[random.randint(0, num_names-1)]
print(f"{random_name} is going to buy the meal tody!")



dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

#nested List
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

col,row = int(position[0]),int(position[1])

map[row - 1][col - 1] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


#Project

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
com_choice = random.randint(0,2)
images = [rock,paper,scissors]



if my_choice < 0 or my_choice > 2:
    print("invalid Input, You lose")
else:
    print(images[my_choice])
    print("Computer chose: ")
    print(images[com_choice])
    if my_choice == com_choice:
        print("It's a draw")
    elif my_choice == 0 and com_choice == 2:
        print("You win")
    elif my_choice == 1 and com_choice == 0:
        print("You win")
    elif my_choice == 2 and com_choice == 1:
        print("You win")
    else:
        print("You lose")


