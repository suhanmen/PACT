def hex_key(num):
    prime_hex_digits = set(['2', '3', '5', '7', 'B', 'D'])
    hex_num = str(num)
    primes_count = 0
    for digit in hex_num:
        if digit in prime_hex_digits:
            # convert hex digit to decimal number
            decimal_num = int(digit, 16)
            if is_prime(decimal_num):
                primes_count += 1
    return primes_count
    
