def hex_key(num):
    primes = {'2', '3', '5', '7', 'B', 'D'} # create set of prime hexadecimal digits
    count = 0 # initialize count to 0
    for digit in num: # loop through each hexadecimal digit
        if digit in primes: # if the digit is prime, increment count
            count += 1
    return count # return the total count of prime hexadecimal digits
