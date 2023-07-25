# list comprehension

numbers = [1, 2, 3]

new_list = [number + 1 for number in numbers]

print(new_list)


name = 'Angela'

new_list2 = [alpha for alpha in name]
print(new_list2)


# challenge 

new_list3 = [n * 2 for n in range(1,5)]
print(new_list3)


# list comprehension with condition

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

short_name = [name for name in names if len(name) <=4]

print(short_name)


long_name_captalize = [name.upper() for name in names if len(name) > 5]

print(long_name_captalize)