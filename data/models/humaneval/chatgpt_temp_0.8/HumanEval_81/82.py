def numerical_letter_grade(grades):
    grades_to_letters = {4.0: "A+", 3.7: "A", 3.3: "A-", 3.0: "B+", 2.7: "B", 2.3: "B-", 2.0: "C+", 1.7: "C", 1.3: "C-", 1.0: "D+", 0.7: "D", 0.0: "D-", -1: "E"}
    letter_grades = []
    for g in grades:
        for grade_value in sorted(grades_to_letters.keys(), reverse=True):
            if g >= grade_value:
                letter_grades.append(grades_to_letters[grade_value])
                break
        else:
            letter_grades.append(grades_to_letters[-1])
    return letter_grades
