def hex_key(num):
    primes = ['2', '3', '5', '7', 'B', 'D'] # prime hexadecimal digits
    count = 0
    for digit in num:
        if digit in primes:
            if int(digit, 16) == 2 or int(digit, 16) == 3: # "2" and "3" are primes
                count += 1
            elif int(digit, 16) % 2 != 0 and int(digit, 16) % 3 != 0: # check for other primes
                count += 1
    return count
