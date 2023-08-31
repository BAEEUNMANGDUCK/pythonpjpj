# Create the logging_decorator() function 👇

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"You Called {func.__name__} ({args[0]}, {args[1]}, {args[2]})")
        print(f"It returned: {func(args[0], args[1], args[2])}")


    return wrapper


# Use the decorator 👇

@logging_decorator
def a_function(one, two, three):
    return one + two + three


a_function(1, 2, 3)
