def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    # Check if the number is negative and convert to positive if necessary
    if num < 0:
        num = abs(num)
    # Convert the number to a string so we can iterate through each digit
    num_str = str(num)
    # Iterate through each digit and determine if it's even or odd
    for digit in num_str:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)
