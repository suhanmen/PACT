def even_odd_count(num):
    """Given an integer, return a tuple that has the number of even and odd digits respectively.

    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    # Convert the integer to a string so we can iterate over its digits
    num_str = str(abs(num))

    # Initialize counters for even and odd digits
    even_count = 0
    odd_count = 0

    # Iterate over each digit in the string
    for digit in num_str:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # If the original number was negative, we need to negate the even and odd counts
    if num < 0:
        even_count *= -1
        odd_count *= -1

    # Return the counts as a tuple
    return (even_count, odd_count)
