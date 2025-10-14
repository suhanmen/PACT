def numerical_letter_grade(grades):
    letter_grades = []
    for g in grades:
        if g == 4.0:
            letter_grades.append('A+')
        elif g > 3.7:
            letter_grades.append('A')
        elif g > 3.3:
            letter_grades.append('A-')
        elif g > 3.0:
            letter_grades.append('B+')
        elif g > 2.7:
            letter_grades.append('B')
        elif g > 2.3:
            letter_grades.append('B-')
        elif g > 2.0:
            letter_grades.append('C+')
        elif g > 1.7:
            letter_grades.append('C')
        elif g > 1.3:
            letter_grades.append('C-')
        elif g > 1.0:
            letter_grades.append('D+')
        elif g > 0.7:
            letter_grades.append('D')
        elif g > 0.0:
            letter_grades.append('D-')
        else:
            letter_grades.append('E')
    return letter_grades
