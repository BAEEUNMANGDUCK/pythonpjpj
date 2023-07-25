import random
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]


students_scores = { name : random.randint(1, 100) for name in names}

print(students_scores)



passed_students = {name: score for name,score in students_scores.items() if score >= 60}

print(passed_students)
