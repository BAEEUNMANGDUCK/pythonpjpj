student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# TODO 1: Create an empty dictionary called student_grades

student_grades = dict()

# TODO 2: Write your code below to add the grades in student_grades

for person in student_scores:

    each_score = student_scores[person]
    if each_score > 90:
        student_grades[person] = "Outstanding"
    elif each_score > 80:
        student_grades[person] = "Exceeds Expectations"
    elif each_score > 70:
        student_grades[person] = "Acceptable"
    else:
        student_grades[person] = "Fail"

print(student_grades)
