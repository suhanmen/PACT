def hex_key(num):
    primes = set(['2', '3', '5', '7', 'B', 'D'])
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
        elif digit.isdigit():
            n = int(digit)
            if n == 1:
                continue
            elif n % 2 == 0:
                continue
            else:
                prime = True
                for i in range(3, int(n ** 0.5) + 1, 2):
                    if n % i == 0:
                        prime = False
                        break
                if prime:
                    count += 1
    return count
