def hex_key(num):
    prime_digits = set(['2', '3', '5', '7', 'B', 'D'])
    count = 0
    # loop through each hexadecimal digit in the input string
    for digit in num:
        # check if the digit is in the set of prime digits
        if digit in prime_digits:
            # if it is, increment the count
            count += 1
    return count
