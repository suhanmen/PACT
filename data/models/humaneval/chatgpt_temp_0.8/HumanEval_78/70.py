def hex_key(num):
    primes = [2, 3, 5, 7, 11, 13, 17]
    count = 0
    for digit in num:
        if digit in ['2', '3', '5', '7', 'B', 'D']:
            decimal = int(digit, 16)
            if decimal in primes:
                count += 1
    return count
