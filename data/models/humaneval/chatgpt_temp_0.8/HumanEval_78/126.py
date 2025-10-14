def hex_key(num):
    primes = set(['2', '3', '5', '7', 'B', 'D'])
    count = 0
    for digit in num:
        if digit in primes:
            if digit in ['B', 'D']:
                if int(num, 16) % 2 != 0 and int(num, 16) % 3 != 0 and int(num, 16) % 5 != 0 and int(num, 16) % 7 != 0 and int(num, 16) % 13 != 0 and int(num, 16) % 17 != 0:
                    count += 1
            else:
                if int(digit) in [2, 3, 5, 7, 11, 13, 17]:
                    count += 1
    return count
