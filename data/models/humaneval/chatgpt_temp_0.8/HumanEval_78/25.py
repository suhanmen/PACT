def hex_key(num):
    # create a set of prime hexadecimal digits
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    
    # initialize a count variable to keep track of prime digits
    prime_digit_count = 0
    
    # loop through each character in the input string
    for digit in num:
        # check if the digit is a prime hexadecimal digit
        if digit in prime_hex_digits:
            # if it is, increment the count variable
            prime_digit_count += 1
    
    # return the final count of prime digits
    return prime_digit_count
