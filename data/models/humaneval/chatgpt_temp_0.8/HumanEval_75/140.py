def is_multiply_prime(a):
    primes = []
    for i in range(2, a):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    if len(primes) < 3:
        return False
    for i in primes:
        for j in primes:
            for k in primes:
                if i * j * k == a:
                    return True
    return False
