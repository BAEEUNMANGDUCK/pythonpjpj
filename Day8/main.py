
import math

# Review
# def greet(name):
#     print(f"hello {name}")
#     print(f"bye {name}")
#     print(f"Goodbye {name}")
#
#
# greet("Angela")

#Position arguments and Keyword arguments
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
#
#
# # Position arguments
greet_with("Bill", "London")

# Keyword argument
greet_with(location="Manchester", name="Gates")

# Area Calc Exercise
test_h = int(input("Height of wall: "))
tesh_w = int(input("Width of wall: "))
coverage = 5


def paint_calc(height, width, cover):
    return math.ceil(height * width / cover)


answer = paint_calc(height=test_h, width=tesh_w, cover=coverage)
print(answer)

# Prime Number Checker
n = int(input("Check this number: "))


def prime_checker(number):
    if number == 2:
        return f"{number} is a prime number"
    for num in range(2, int(number ** 0.5) + 1):
        if number % num == 0:
            return f"{number} is not a prime number"
    return f"{number} is a prime number"


print(prime_checker(number=n))
