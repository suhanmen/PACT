def hex_key(num):
    primes = set(['2', '3', '5', '7', 'B', 'D'])
    count = 0
    for digit in num:
        if digit in primes:
            if digit in ['B', 'D']:
                if int(num, 16) % 2 == 0 or int(num, 16) % 3 == 0:
                    continue
                elif int(num, 16) == 5 or int(num, 16) == 7:
                    count += 1
                elif int(num, 16) < 11:
                    count += 1
                elif int(num, 16) % 5 == 0 or int(num, 16) % 7 == 0:
                    continue
                else:
                    count += 1
            else:
                count += 1
    return count
