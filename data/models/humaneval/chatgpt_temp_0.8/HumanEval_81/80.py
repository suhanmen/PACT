def numerical_letter_grade(grades):
    grade_scale = {
        4.0: 'A+',
        3.7: 'A',
        3.3: 'A-',
        3.0: 'B+',
        2.7: 'B',
        2.3: 'B-',
        2.0: 'C+',
        1.7: 'C',
        1.3: 'C-',
        1.0: 'D+',
        0.7: 'D',
        0.0: 'D-',
        -1: 'E'
    }
    letter_grades = []
    for g in grades:
        if g >= 4:
            letter_grades.append(grade_scale[4.0])
        elif g >= 3.7:
            letter_grades.append(grade_scale[3.7])
        elif g >= 3.3:
            letter_grades.append(grade_scale[3.3])
        elif g >= 3.0:
            letter_grades.append(grade_scale[3.0])
        elif g >= 2.7:
            letter_grades.append(grade_scale[2.7])
        elif g >= 2.3:
            letter_grades.append(grade_scale[2.3])
        elif g >= 2.0:
            letter_grades.append(grade_scale[2.0])
        elif g >= 1.7:
            letter_grades.append(grade_scale[1.7])
        elif g >= 1.3:
            letter_grades.append(grade_scale[1.3])
        elif g >= 1.0:
    
