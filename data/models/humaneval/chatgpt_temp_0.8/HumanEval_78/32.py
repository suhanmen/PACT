def hex_key(num):
    primes = ['2', '3', '5', '7', 'B', 'D']  # list of prime hex digits
    count = 0  # count of prime hex digits
    for digit in num:  # loop through each digit in the input
        if digit in primes:  # if the digit is prime
            count += 1  # increment the count
    return count  # return the count of prime hex digits
