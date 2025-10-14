def even_odd_count(num):
    even_count = 0
    odd_count = 0
    # Convert the integer to a string so we can loop through its digits
    num_str = str(abs(num))
    for digit in num_str:
        # Check if the digit is even or odd
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    # Return a tuple of the even and odd counts
    return (even_count, odd_count)
