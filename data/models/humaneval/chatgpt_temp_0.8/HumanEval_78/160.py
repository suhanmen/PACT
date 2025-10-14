def hex_key(num):
    prime_hex_digits = ['2', '3', '5', '7', 'B', 'D'] # list of prime hexadecimal digits
    count = 0 # initialize count of prime digits to zero
    
    # loop through each hexadecimal digit in the input string
    for digit in num:
        # check if the digit is a prime hexadecimal digit
        if digit in prime_hex_digits:
            # if it is, increment the count
            count += 1
    
    return count
