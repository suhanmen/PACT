def hex_key(num):
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    prime_count = 0
    for digit in num:
        if digit in prime_hex_digits:
            prime_count += 1
    return prime_count
