def hex_key(num):
    primes = set(['2', '3', '5', '7', 'B', 'D'])
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
        else:
            try:
                n = int(digit, 16)
                if n > 1:
                    is_prime = True
                    for i in range(2, int(n ** 0.5) + 1):
                        if n % i == 0:
                            is_prime = False
                            break
                    if is_prime:
                        count += 1
            except ValueError:
                pass
    return count
