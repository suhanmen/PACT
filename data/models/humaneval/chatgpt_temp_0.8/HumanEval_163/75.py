def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # create an empty list to store the even digits
    even_digits = []

    # iterate through the range of numbers from a to b
    for i in range(a, b+1):
        # check if the number contains even digits
        for digit in str(i):
            if int(digit) % 2 == 0:
                even_digits.append(i)
                break

    # return the list of even digits in ascending order
    return sorted(even_digits)
