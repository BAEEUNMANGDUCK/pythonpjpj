import time
# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# # 함수가 First-class objects로 취급되어 인자로 전달될 수 있다.
#
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
#
# result = calculate(add, 2, 3)
# print(result)
#
#
# # Nested Functions
#
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     nested_function()
#
#
# outer_function()
#
# # Functions can be returned from other functions
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
#
#
# inner_function = outer_function()
# inner_function()
import time


# Python Decorator Function --> 다른 함수를 감싸 추가 기능을 부여하는 함수

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")


decorated_function = delay_decorator(say_greeting)
decorated_function()
say_hello()