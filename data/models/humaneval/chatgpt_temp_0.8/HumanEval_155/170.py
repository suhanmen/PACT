def even_odd_count(num):
    even_count = 0
    odd_count = 0
    # convert the number to a string
    num_str = str(num)
    # iterate through each digit
    for digit in num_str:
        # check if the digit is even or odd
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    # return the counts as a tuple
    return (even_count, odd_count)
