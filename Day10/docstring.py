def format_name(f_name, l_name):
    """ Take a first and last name and format it to return the title case version of name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid input"  # early return
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"


my_name = format_name(f_name="KIM", l_name="EUNBAE")
my_name2 = format_name(input('what is your first name?'), input("what is your last name?"))


# 각 함수에 짧은 설명을 docstrng으로 할 수 있음.