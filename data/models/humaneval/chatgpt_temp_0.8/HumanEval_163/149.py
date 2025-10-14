def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    even_digits = []
    if a > b:
        a, b = b, a  # swap values if a is greater than b
    for num in range(a, b+1):
        digits = [int(digit) for digit in str(num)]  # convert number to a list of digits
        for digit in digits:
            if digit % 2 == 0:
                even_digits.append(digit)
    return sorted(list(set(even_digits)))  # remove duplicates and sort in ascending order
