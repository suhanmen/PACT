def unique_digits(x):
    """
    Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.
    """
    result = []
    for num in x:
        no_even_digit = True
        for digit in str(num):
            if int(digit) % 2 == 0:
                no_even_digit = False
                break
        if no_even_digit:
            result.append(num)
    return sorted(result)
