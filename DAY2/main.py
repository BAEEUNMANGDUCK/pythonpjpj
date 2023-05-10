#Data types

#String

print("Hello"[0]) # H
print("Hello"[4]) # o
print("123" + "456") #123456,  String, not a number

#Integer

print(123 + 456) #579
print(123_456_789)

#Float

print(3.14159)

#Boolean 

print(True)
print(False)

#  str + int --> Error, str + str(int) --> OK
num_char = len(input("what is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = 123 
type(a) # int
type(str(a)) # str

#Example 1 
two_digit_number = input("Type a two digit number: ")
first_num = int(two_digit_number[0])
second_num = int(two_digit_number[1])
result = first_num + second_num
print(result)


# +, -, *, /, **, //, % --> python operator '/' 는 float 으로 값이 반환됨, 괄호를 치면 연산 우선순위를 높일 수 있음



#BMI CALCULATOR

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(float(weight) / (float(height) ** 2)) 
print(bmi)


print(round(8/3)) #반올림
print(8//3) #정수 부분만

#f-string
score = 0 
height = 1.8
isWinning = True
print(f"your score is {score}")
print(f"your height is {height}")
print(f"your winning is {isWinning}")

#Example 2  Your Life in weeks

# age = input("What is your current age?: ")
# new_age = int(age)
# left_days = (90 * 365) - (new_age * 365) 
# left_weeks = (90 * 52) - (new_age * 52)
# left_months = (90 * 12) - (new_age * 12)

# result = f"You have {left_days} days, {left_weeks} weeks and {left_months} months left."
# print(result)

#Final Project

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip_percentage = (int(input("What percentage tip would you like to give? 10, 12, or 15: "))/100) + 1
no_of_peoples = int(input("How many people to split the bill? "))
pay_each = f"Each person should pay: ${total_bill * tip_percentage / no_of_peoples:.2f}"
print(pay_each)