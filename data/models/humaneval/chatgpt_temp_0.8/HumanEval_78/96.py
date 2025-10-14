def hex_key(num):
    primes = set(['2', '3', '5', '7', 'B', 'D'])
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isdigit():
            if int(digit) in [1, 4, 6, 8, 9]:
                continue
            if int(digit) == 0 or int(digit) == 2 or int(digit) == 5 or int(digit) == 7:
                count += 1
            else:
                n = int(digit)
                if n > 7:
                    n -= 10
                if n in [1, 3, 7, 9, 11, 13, 17]:
                    count += 1
    return count
