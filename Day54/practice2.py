# 파이썬 함수 실행 시간 측정 with python decorator
import time

current_time = time.time()
# print(current_time)


def speed_calc_decorator(func):

    def wrapper_function():
        start = current_time
        func()
        end = time.time()
        print(f"{func.__name__}:{end - start}")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
