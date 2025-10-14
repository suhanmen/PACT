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

    # iterate through the range of numbers between a and b
    for num in range(min(a, b), max(a, b)+1):

        # convert the number to a string to access each digit
        num_str = str(num)

        # iterate through each digit in the number
        for digit in num_str:

            # check if the digit is even and not already in the list
            if int(digit) % 2 == 0 and int(digit) not in even_digits:

                # add the even digit to the list
                even_digits.append(int(digit))

    # return the list of even digits in ascending order
    return sorted(even_digits)
