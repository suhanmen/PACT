def numerical_letter_grade(grades):
    result = []
    for grade in grades:
        if grade == 4:
            result.append('A+')
        elif grade > 3.7:
            result.append('A')
        elif grade > 3.3:
            result.append('A-')
        elif grade > 3.0:
            result.append('B+')
        elif grade > 2.7:
            result.append('B')
        elif grade > 2.3:
            result.append('B-')
        elif grade > 2.0:
            result.append('C+')
        elif grade > 1.7:
            result.append('C')
        elif grade > 1.3:
            result.append('C-')
        elif grade > 1.0:
            result.append('D+')
        elif grade > 0.7:
            result.append('D')
        elif grade > 0:
            result.append('D-')
        else:
            result.append('E')
    return result
