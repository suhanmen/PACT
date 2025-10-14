def hex_key(num):
    primes = set(['2', '3', '5', '7', 'B', 'D']) # set of prime hexadecimal digits
    count = 0 # variable to keep track of count of prime digits
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isdigit():
            # check if the decimal equivalent of the digit is a prime number
            decimal_digit = int(digit, 16) # convert hexadecimal digit to decimal
            if decimal_digit > 1:
                for i in range(2, int(decimal_digit ** 0.5) + 1):
                    if decimal_digit % i == 0:
                        break
                else:
                    count += 1
    return count
