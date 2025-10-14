def even_odd_count(num):
    even_digits = 0
    odd_digits = 0
    # convert the integer to a string so we can iterate over its digits
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even_digits += 1
        else:
            odd_digits += 1
    # return the counts as a tuple
    return (even_digits, odd_digits)
