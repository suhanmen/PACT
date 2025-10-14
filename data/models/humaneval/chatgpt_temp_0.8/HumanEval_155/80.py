def even_odd_count(num):
    """
    Given an integer, return a tuple that has the number of even and odd digits respectively.

    Example:
    even_odd_count(-12) ==> (1, 1)
    even_odd_count(123) ==> (1, 2)
    """
    even_count = odd_count = 0 # Initialize the counters
    num = abs(num) # Convert negative number to positive
    while num > 0:
        digit = num % 10 # Get the last digit
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num //= 10 # Remove the last digit
    return (even_count, odd_count) # Return the tuple
