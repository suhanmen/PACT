def hex_key(num):
    primes = set(['2', '3', '5', '7', 'B', 'D'])
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isalpha():
            decimal_value = int(digit, 16)
            if decimal_value in [11, 13, 17]:
                count += 1
    return count
