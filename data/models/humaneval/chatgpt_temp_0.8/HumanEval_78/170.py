def hex_key(num):
    primes = {"2", "3", "5", "7", "B", "D"} # set of prime hexadecimal digits
    count = 0 # initialize count to 0
    for digit in num:
        if digit in primes:
            count += 1
    return count
