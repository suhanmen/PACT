def hex_key(num):
    primes = set(['2', '3', '5', '7', 'B', 'D']) # set of prime hex digits
    count = 0 # counter for prime digits
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isdigit() and int(digit) > 1:
            for i in range(2, int(digit)):
                if int(digit) % i == 0:
                    break # not a prime
            else:
                count += 1 # is a prime
    return count
