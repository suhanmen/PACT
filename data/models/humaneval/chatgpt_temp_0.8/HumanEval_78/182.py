def hex_key(num):
    hex_primes = set(['2', '3', '5', '7', 'B', 'D'])
    count = 0
    for digit in num:
        if digit in hex_primes:
            count += 1
        elif digit.isdigit():
            if int(digit) in [2, 3, 5, 7]:
                count += 1
    return count
