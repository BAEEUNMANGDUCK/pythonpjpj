# number = int(input("Which number do you want to check?"))
#
# if number % 2 = 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# 해당 코드의 문제점: if 문의 조건문에는 비교연산자가 들어와야 하는데 number % 2 = 0 이라는 대입 연산자가 들어가 있음. 따라서 = 을 == 으로 고쳐야 함.
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")