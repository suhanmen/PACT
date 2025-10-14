def hex_key(num):
    primes = set(['2','3','5','7','B','D']) # set of prime hexadecimal digits
    count = 0 # initialize count of prime digits to 0
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isdigit() and int(digit) > 1: # check if non-prime digit is greater than 1
            for i in range(2, int(digit)):
                if int(digit) % i == 0:
                    break # not a prime, move on to next digit
            else: # loop did not hit break statement, so digit is a prime
                count += 1
    return count
