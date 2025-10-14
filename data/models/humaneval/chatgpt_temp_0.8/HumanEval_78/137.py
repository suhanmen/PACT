def hex_key(num):
    primes = set(['2', '3', '5', '7', 'B', 'D'])
    count = 0
    for digit in num:
        if digit in primes:
            if digit in ['B', 'D']:
                # convert B or D to decimal and check if it's prime
                decimal = int(digit, 16)
                if is_prime(decimal):
                    count += 1
            else:
                # convert digit to decimal and check if it's prime
                decimal = int(digit, 16)
                if is_prime(decimal):
                    count += 1
    return count
