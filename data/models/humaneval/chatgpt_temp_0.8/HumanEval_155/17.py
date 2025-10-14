def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Convert the integer to a string to access individual digits
    num_str = str(num)
    
    # Initialize counters for even and odd digits
    even_count = 0
    odd_count = 0
    
    # Loop through each digit in the string
    for digit in num_str:
        # Convert digit back to an integer
        digit_int = int(digit)
        # Check if the digit is even
        if digit_int % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # Return a tuple with the even and odd counts
    return (even_count, odd_count)
