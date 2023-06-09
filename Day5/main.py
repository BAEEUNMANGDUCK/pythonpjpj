# fruits = ["Apple", "Peach", "Pear"]
#
# # for 문 - 반복가능한 객체의 요소를 반환
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
#
# print(fruits)

# Average Height

# student_heights = input("Input a list of student height: ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
#
#
# # for 문을 사용하여 평균 키를 구하는 방법(조건: len()과 sum() 함수 쓰지 않고)
# people_count = 0
# height_sum = 0
# for height in student_heights:
#     height_sum += height
#     people_count += 1
#
# average_height = round(height_sum / people_count)
# print(f"average height is {average_height} cm!")
#
# # for 문을 이용해 가장 높은 점수를 구하기(조건: max() 함수 쓰지 않고)
#
# student_scores = input("Input a list of studetn scores: ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# # print(student_scores)
#
# max_value = 0
# for score in student_scores:
#     if score > max_value:
#         max_value = score
#     else:
#         pass
#
# print(f"the highest score is {max_value}!")


#  1 부터 101까지의 합 구하기 (range, for 문 사용해서)

# sum = 0
# for num in range(1, 101):
#     sum += num
#
# print(sum)


# 1 부터 100까지의 모든 짝수의 합계 구하기
# even_sum = 0
#
# for num in range(1, 101):
#     if num % 2 == 0:
#         even_sum += num
#
# print(f"even_sum is : {even_sum}")

# FizzBuzz 게임
# 규칙: 1~100까지의 숫자 중에 3으로 나눌 수 있으면 'Fizz', 5로 나눌 수 있으면 'Buzz', 3과 5 둘다 나눌 수 있으면 FizzBuzz라고 외친다
#
# for num in range(1, 101):
#     if num % 3 == 0 and num % 5== 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# 비밀번호 생성기 만들기

import string
import random

alphabet = list(string.ascii_lowercase + string.ascii_uppercase)
numbers = [str(num) for num in range(10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

how_many_letters = int(input("How many letters would you like in your password? \n"))
how_many_symbols = int(input("How many symbols would you like?\n"))
how_many_numbers = int(input("How many numbers would you like?\n"))

get_letters = [random.choice(alphabet) for _ in range(how_many_letters)]
get_symbols = [random.choice(symbols) for _ in range(how_many_symbols)]
get_numbers = [random.choice(numbers) for _ in range(how_many_numbers)]

all_things = get_letters + get_symbols + get_numbers
random.shuffle(all_things)
password = "".join(all_things)

print(f"password is : {password}")
