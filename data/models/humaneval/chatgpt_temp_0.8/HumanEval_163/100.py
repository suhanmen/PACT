def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # create a list to store the even digits between a and b
    result = []

    # make sure a is smaller than b
    if a > b:
        a, b = b, a

    # iterate through the range between a and b, inclusive
    for num in range(a, b+1):
        # convert the number to a string and iterate through its digits
        for digit in str(num):
            # check if the digit is even and not already in the result list
            if int(digit) % 2 == 0 and int(digit) not in result:
                result.append(int(digit))

    return result
