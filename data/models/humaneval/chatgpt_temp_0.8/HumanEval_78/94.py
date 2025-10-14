def hex_key(num):
    primes = set(['2', '3', '5', '7', 'B', 'D'])
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
        elif digit == 'A':
            continue
        elif digit == 'C':
            continue
        elif digit == 'E':
            continue
        elif digit == 'F':
            continue
        else:
            return "Invalid input"
    return count
