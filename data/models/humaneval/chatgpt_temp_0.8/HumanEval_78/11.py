def hex_key(num):
    primes = ['2', '3', '5', '7', 'B', 'D']
    count = 0
    for c in num:
        if c in primes:
            count += 1
    return count
