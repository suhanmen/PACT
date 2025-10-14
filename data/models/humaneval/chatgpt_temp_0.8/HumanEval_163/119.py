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

    # make sure a is less than or equal to b
    if a > b:
        a, b = b, a

    # loop through the range from a to b
    for i in range(a, b + 1):
        # convert i to a string so we can loop through its digits
        s = str(i)
        for c in s:
            # check if the digit is even and not already in the list
            if c.isdigit() and int(c) % 2 == 0 and int(c) not in even_digits:
                even_digits.append(int(c))

    # sort the list in ascending order
    even_digits.sort()

    return even_digits
