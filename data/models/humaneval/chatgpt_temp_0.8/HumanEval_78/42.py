def hex_key(num):
    primes = {'2', '3', '5', '7', 'B', 'D'}
    count = 0
    for digit in num:
        if digit in primes:
            if digit in {'B', 'D'}:
                # Convert hexadecimal digit to decimal
                decimal = int(digit, 16)
                # Check if decimal digit is prime
                if decimal in {2, 3, 5, 7, 11, 13, 17}:
                    count += 1
            else:
                count += 1
    return count
