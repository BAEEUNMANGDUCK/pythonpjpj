# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# age = int(input("How old are you?"))
# price = 0

##if-else,comparison operator

# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

#Even or Odd

# number = int(input("Which number do you want to check? "))

# if number % 2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")

##nested if

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

##BMI 2.0

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
# bmi = round(weight / (height ** 2))

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.") 
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you are normalweight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese")

##Leap year or not

# year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


    
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     if age < 12:
#         price  = 5
#         print("Please pay $5.")
#     elif age <= 18:
#         price = 7
#         print("Please pay $7.")
#     elif age >= 45 and age <=55:
#         price = 0
#         print("midlife pay $0.")
#     else:
#         price = 12
#         print("Please pay $12.")
#     wants_photo = input("Do you want a photo taken? press Y or N: ").lower()
#     if wants_photo == 'y':
#         price += 3    
#     print(f"Your final bill is {price}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want S, M or L: ").lower()
# add_pepperoni = input("Do you want pepperoni? Y or N: ").lower()
# extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
# final_bill = 0 

# if size == 's':
#     final_bill += 15
# elif size == 'm':
#     final_bill += 20
# elif size == 'l':
#     final_bill += 25
# else:
#     print("You write wrong ")


# if add_pepperoni == 'y':
#     if size == 's':
#         final_bill += 2
#     else:
#         final_bill += 3

# if extra_cheese == 'y':
#     final_bill += 1

# print(f"Your final bill is: ${final_bill}.")



#Love Calculator

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# lower_name1 = name1.lower()
# lower_name2 = name2.lower()
# concat_names = lower_name1 + lower_name2
# print(concat_names)

# #true love
# count_true = concat_names.count('t') + concat_names.count('r') + concat_names.count('u') + concat_names.count('e')
# count_love = concat_names.count('l') + concat_names.count('o') + concat_names.count('v') + concat_names.count('e')
# score = int(str(count_true) + str(count_love))

# if score < 10 or score > 90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif score >= 40 and score <= 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}")


#Project treasure island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

cross_load = input("left or right? ").lower()
if cross_load == "right":
    print("You fell in to a hole. Game over!")
else:
    island = input("You come to a lake. There is an island in the middle of the lake, Type 'swim' or 'wait' ").lower()
    if island == 'wait':
        doors = input("There are three doors. Yellow one, Blue one and Red one. choose one color! ").lower()
        if doors == 'yellow':
            print("You win")
        elif doors == 'red':
            print("There are so many beasts Game over!")
        else:
            print("There are so many bugs Game over!")
    else:
        print("There are so many alligators Game over!")

