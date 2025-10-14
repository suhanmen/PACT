def hex_key(num):
    prime_set = set(['2', '3', '5', '7', 'B', 'D'])
    count = 0
    for digit in num:
        if digit in prime_set:
            if digit in ['B', 'D']:  # Convert B and D to the corresponding decimal value
                digit = int(digit, 16)
            else:
                digit = int(digit)
            if is_prime(digit):
                count += 1
    return count

