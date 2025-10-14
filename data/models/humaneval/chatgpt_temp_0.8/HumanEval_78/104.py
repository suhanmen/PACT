def hex_key(num):
    primes = set(['2', '3', '5', '7', 'B', 'D'])
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isdigit():
            if int(digit) in [1, 4, 6, 8, 9]:
                continue
            elif int(digit) == 2:
                count += 1
            elif int(digit) % 2 == 0:
                continue
            else:
                is_prime = True
                for i in range(3, int(int(digit)**0.5)+1, 2):
                    if int(digit) % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    count += 1
    return count
