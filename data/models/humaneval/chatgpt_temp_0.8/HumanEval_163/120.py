def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # initialize empty list to store even digits
    even_digits = []
    # loop through all the numbers between a and b (inclusive)
    for num in range(a, b+1):
        # convert the number to a string to access its digits
        digits = str(num)
        # loop through each digit in the number
        for digit in digits:
            # check if the digit is even and not already in the list
            if int(digit) % 2 == 0 and int(digit) not in even_digits:
                # add the digit to the list
                even_digits.append(int(digit))
    # sort the list in ascending order
    even_digits.sort()
    # return the list of even digits
    return even_digits
