student_scores = {
    'Harry': 81,
    'Ron': 78,
    'Hermione': 99,
    'Draco': 74,
    'Neville': 64,
}


def grader(student_scores):
    student_grades = {}

    for students in student_scores:
        grade = student_scores[students]
        if grade > 90:
            student_grades[students] = 'Outstanding'
        elif grade > 80:
            student_grades[students] = 'Exceeds expectation'
        elif grade > 70:
            student_grades[students] = 'Acceptable'
        else:
            student_grades[students] = 'Fail'
    return student_grades

