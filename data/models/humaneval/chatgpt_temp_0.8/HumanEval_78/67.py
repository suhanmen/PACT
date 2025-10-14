def hex_key(num):
    primes = ['2', '3', '5', '7', 'B', 'D'] # list of prime hexadecimal digits
    count = 0 # initialize count to 0
    for digit in num:
        if digit in primes:
            count += 1 # increment count if digit is prime
    return count
