def hex_key(num):
    primes = set(['2', '3', '5', '7', 'B', 'D'])
    count = 0
    
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isalpha():
            # convert letter to decimal number
            decimal_num = int(digit, 16)
            # check if decimal number is prime
            if decimal_num > 1:
                for i in range(2, decimal_num):
                    if decimal_num % i == 0:
                        break
                else:
                    count += 1
                    
    return count
