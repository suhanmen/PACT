def hex_key(num):
    primes = [2, 3, 5, 7, 11, 13, 17]
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    count = 0
    
    for digit in num:
        if digit in hex_digits:
            decimal_value = int(digit, 16)
            if decimal_value in primes:
                count += 1
                
    return count
