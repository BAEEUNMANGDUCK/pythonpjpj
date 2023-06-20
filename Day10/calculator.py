from art import logo




# Calculator

# ADD
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


# Print VS Return

# Return을 하면 호출된 곳으로 값이 전달되고 변수에 전달되면 다른 곳에 활용이 가능
def calculator():
    print(logo)
    end_of_operation = False
    num1 = float(input("What's the first number?: "))
    for op in operations:
        print(op)

    while not end_of_operation:
        op_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        op_function = operations[op_symbol]
        answer = op_function(num1, num2)
        print(f"{num1} {op_symbol} {num2} = {answer}")

        yes_or_no = input(
            f"Type 'y' to continue calculating with {num1} or type 'n' to start a new calculations or type 'q' to stop : ").lower()
        if yes_or_no == 'y':
            num1 = answer
        elif yes_or_no == 'n':
            end_of_operation = True
            calculator()
        else:
            end_of_operation = True
    # print("bye")
calculator()
