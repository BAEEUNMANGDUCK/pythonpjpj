# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])


# 이 코드의 문제점:
# 먼저 FizzBuzz를 출력하기 위한 조건이 숫자가 3과 5로 모두 나누어져야 하는 조건인데, or 이라는 논리 연산자로 연결되어 있기에 and로 바꿔줘야 함.
# 또한 하나의 조건에만 충족하여 명령문이 실행되어야 함. 따라서 if - elif -elif - else 로 바꿔줘야 함.
# 즉, 코드 상으로는 문제가 없지만 논리적인 오류를 고쳐야 함.
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print([number])
