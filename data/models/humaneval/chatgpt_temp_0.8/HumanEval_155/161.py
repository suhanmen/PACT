def even_odd_count(num):
    """
    Given an integer, return a tuple that has the number of even and odd digits respectively.

    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Convert the integer to a string to easily iterate through each digit
    num_str = str(abs(num))

    # Initialize counters for even and odd digits
    even_count = 0
    odd_count = 0

    # Iterate through each digit in the string
    for digit in num_str:
        # If the digit is even, increment the even count
        if int(digit) % 2 == 0:
            even_count += 1
        # If the digit is odd, increment the odd count
        else:
            odd_count += 1

    # Return a tuple with the even count and odd count
    return (even_count, odd_count)
