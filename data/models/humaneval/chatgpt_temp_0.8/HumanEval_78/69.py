def hex_key(num):
    primes = set(['2', '3', '5', '7', 'B', 'D'])
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isalpha() and ord(digit) - ord('A') > 5:
            # If a hex digit is not prime and it's not one of A, C, E, we can
            # skip the next digit because it cannot be prime.
            count += 1
        elif int(digit) > 1 and all(int(digit) % i != 0 for i in range(2, int(digit))):
            count += 1
    return count
