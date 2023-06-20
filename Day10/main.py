# More about function


# Functions with Outputs

def my_function():
    return 3 * 2


output = my_function()
print(output)


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid input"  # early return
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"


my_name = format_name(f_name="KIM", l_name="EUNBAE")
my_name2 = format_name(input('what is your first name?'), input("what is your last name?"))

print(my_name)
print(my_name2)
