def hex_key(num):
    primes = ['2', '3', '5', '7', 'B', 'D'] # list of prime hex digits
    count = 0 # initialize count variable
    for digit in num: # iterate through each digit in the input string
        if digit in primes: # check if the digit is prime
            count += 1 # if it is, increment the count
    return count # return the count of prime hex digits
