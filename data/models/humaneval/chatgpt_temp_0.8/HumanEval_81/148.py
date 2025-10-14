def numerical_letter_grade(grades):
    letter_grades = []
    for GPA in grades:
        if GPA == 4.0:
            letter_grades.append('A+')
        elif GPA > 3.7:
            letter_grades.append('A')
        elif GPA > 3.3:
            letter_grades.append('A-')
        elif GPA > 3.0:
            letter_grades.append('B+')
        elif GPA > 2.7:
            letter_grades.append('B')
        elif GPA > 2.3:
            letter_grades.append('B-')
        elif GPA > 2.0:
            letter_grades.append('C+')
        elif GPA > 1.7:
            letter_grades.append('C')
        elif GPA > 1.3:
            letter_grades.append('C-')
        elif GPA > 1.0:
            letter_grades.append('D+')
        elif GPA > 0.7:
            letter_grades.append('D')
        elif GPA > 0.0:
            letter_grades.append('D-')
        else:
            letter_grades.append('E')
    return letter_grades
