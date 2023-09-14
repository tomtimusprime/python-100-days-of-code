student_scores = { "Harry": 81,
                    "Hermione": 99,
                    "Ron" : 78,
                    "Draco" : 72,
                    "Neville" : 68
                 }

student_grades = {
    "Harry": 81,
    "Hermione": 99,
    "Ron" : 78,
    "Draco" : 72,
    "Neville" : 88
}

for key in student_scores:
    if student_scores[key] > 91:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81:
        student_grades[key] = "Solid Job"
    elif student_scores[key] >= 71:
        student_grades[key] = "Acceptable"
    elif student_scores[key] >= 61:
        student_grades[key] = "Poor Performane"

for key in student_grades:
    print(key)
    print(student_grades[key])