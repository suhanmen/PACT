def hex_key(num):
    primes = ['2', '3', '5', '7', 'B', 'D'] # list of prime hexadecimal digits
    count = 0 # initialize count to 0
    for digit in num: # loop through each digit in the input string
        if digit in primes: # if the digit is a prime hexadecimal digit
            count += 1 # increment the count
    return count # return the count of prime hexadecimal digits
