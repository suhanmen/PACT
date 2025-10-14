def hex_key(num):
    # list of prime hexadecimal digits
    primes = ['2', '3', '5', '7', 'B', 'D']
    
    # convert hexadecimal number to a list of digits
    digits = list(num)
    
    # count the number of prime digits in the hexadecimal number
    count = 0
    for digit in digits:
        if digit in primes:
            count += 1
    
    return count
