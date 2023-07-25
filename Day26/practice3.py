with open('file1.txt', mode='r') as file1:
    content = file1.readlines()
    file1_list = [ int(num.strip()) for num in content ]
    
with open('file2.txt', mode='r') as file2:
    content = file2.readlines()
    file2_list = [ int(num.strip()) for num in content ]


result = [ num for num in file1_list if num in file2_list]


print(result)


# Refactoring us-states-game using list comprehension 

# # BEFORE
# if answer_state == "Exit":
#     missing_states = []
#     for state in all_states:
#         if state not in guessed_states:
#             missing_states.append(state)
            
# # AFTER    
# missing_states = [ state for state in all_states if state not in gussed_states] 