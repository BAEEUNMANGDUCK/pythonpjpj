# Debugging

############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# Describe Problem
# 위의 값이 출력되지 않는 이유는? range(1, 20)은 1부터 19까지만 i에 대입된다. 따라서 21로 고쳐줘야 값이 출력됨.
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])


# Reproduce the Bug
# 의도적으로 오류를 발생시키도록 재현하기 => 인덱스가 6이면 IndexError로 오류가 항상남
# 따라서 dice_imgs의 이미지를 출력할 때, 오류가 나지 않기 위해서는 randint의 인자가 0과 5이어야 함.

from random import randint

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[6])

dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# Play Computer
# 이 코드의 문제의 문제점, 첫번째 조건은 1981년부터 1993년까지만 해당함. 하지만 millenial은 1980년부터 1994년임
# 따라서 크거나 같다, 작거나 같다로 부등호를 줘야 함.
year = int(input("What's your year of birth?"))
if 1980 <= year <= 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}

# Fix the Errors
# 편집기의 오류 표시, 콘솔의 오류표시를 주의 깊게 보기, 먼저 print()의 들여쓰기가 잘못됐을 때 빨간줄 표시가 나기때문에 고침
# 그리고 age에 숫자를 넣어도 조건문이 오류를 발생하여 콘솔에 str과 int를 비교할 수 없다고 나오기 때문에 input 값이 str이라는 것을 알 수 있음
# 따라서 age 값을 int로 바꿈, f 스트링으로 print 안의 문장을 고쳐야 함.
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# Print is Your Friend
# pages 값과 word_per_page 값이 곱해져서 대입되어야 할 total_words 값이 0으로 출력됨.
#  == 는 비교 연산자이기때문에 오류가 발생함. 따라서 = 로 바꿔줘야 함.
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)


# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])


# Use a Debugger
# 디버거를 사용하면, b_list.append(new_item)값으로 각각의 값이 곱해지고, b_list에 들어가지 않고
# for문이 반복가능한 객체를 모두 반환한 후에 마지막에 저장된 new_item 값이 b_list값에 들어가는 것을 볼 수 있음.
# 따라서 해당 함수의 문제점은 b_list.append(new_item)의 들여쓰기가 잘못된 것임.
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
# 의도하는 값 [2, 4, 6, 10, 16, 26] 임.