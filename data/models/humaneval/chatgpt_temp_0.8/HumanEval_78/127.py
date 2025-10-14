def hex_key(num):
    # Set of prime hexadecimal digits
    prime_hex = set(['2', '3', '5', '7', 'B', 'D'])
    # Convert the hexadecimal number to a set of digits
    hex_digits = set(num.upper())
    # Return the number of prime hexadecimal digits
    return len(prime_hex.intersection(hex_digits))
