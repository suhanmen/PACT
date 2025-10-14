def unique_digits(x):
    """
    Given a list of positive integers x, return a sorted list of all
    elements that have no even digits.

    :param x: list of positive integers
    :return: sorted list of integers with no even digits
    """
    result = []
    
    for num in sorted(x):
        digits = set(str(num))
        if not any(int(digit) % 2 == 0 for digit in digits):
            result.append(num)
    
    return result
