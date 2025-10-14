def hex_key(num):
    primes = {'2', '3', '5', '7', 'B', 'D'}
    prime_count = 0
    for digit in num:
        if digit in primes:
            prime_count += 1
    return prime_count
