def hex_key(num):
    primes = {'2', '3', '5', '7', 'B', 'D'}  # set of prime hexadecimal digits
    count = 0  # initialize count of prime digits to 0
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isalpha() and int(digit, 16) > 13:
            # if the digit is not a prime, but is a letter and has a value greater than 13,
            # we can skip all the remaining digits since they will also be greater than 13
            break
    return count
