def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    even_count = 0
    odd_count = 0

    # Convert the integer to a string for easy iteration over its digits
    num_str = str(num)

    # Iterate over each digit in the string
    for digit in num_str:
        # If the digit is even, increment the even count
        if int(digit) % 2 == 0:
            even_count += 1
        # If the digit is odd, increment the odd count
        else:
            odd_count += 1

    # Return a tuple with the even and odd count respectively
    return (even_count, odd_count)
