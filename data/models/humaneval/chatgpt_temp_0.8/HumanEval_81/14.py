def numerical_letter_grade(grades):
    letter_grades = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade = 'A+'
        elif gpa > 3.7:
            letter_grade = 'A'
        elif gpa > 3.3:
            letter_grade = 'A-'
        elif gpa > 3.0:
            letter_grade = 'B+'
        elif gpa > 2.7:
            letter_grade = 'B'
        elif gpa > 2.3:
            letter_grade = 'B-'
        elif gpa > 2.0:
            letter_grade = 'C+'
        elif gpa > 1.7:
            letter_grade = 'C'
        elif gpa > 1.3:
            letter_grade = 'C-'
        elif gpa > 1.0:
            letter_grade = 'D+'
        elif gpa > 0.7:
            letter_grade = 'D'
        elif gpa > 0.0:
            letter_grade = 'D-'
        else:
            letter_grade = 'E'
        letter_grades.append(letter_grade)
    return letter_grades
