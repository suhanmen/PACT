def numerical_letter_grade(grades):
    # create a list of tuples containing the lower bound of each grade range and its corresponding letter grade
    grade_ranges = [(4.0, 'A+'), (3.7, 'A'), (3.3, 'A-'), (3.0, 'B+'), (2.7, 'B'), (2.3, 'B-'), (2.0, 'C+'), (1.7, 'C'), (1.3, 'C-'), (1.0, 'D+'), (0.7, 'D'), (0.0, 'D-')]
    
    letter_grades = []  # initialize an empty list to store the letter grades
    
    for grade in grades:
        for i in range(len(grade_ranges)):
            if grade >= grade_ranges[i][0]:
                letter_grades.append(grade_ranges[i][1])
                break  # break out of the inner loop once the correct letter grade is found
    
    return letter_grades
