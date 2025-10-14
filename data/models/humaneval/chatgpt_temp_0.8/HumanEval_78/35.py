def hex_key(num):
    # A set of prime digits in hexadecimal number system
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    
    # Count the number of prime digits in the input hexadecimal number
    count = 0
    for digit in num:
        if digit in prime_hex_digits:
            count += 1
            
    return count
