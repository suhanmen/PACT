def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for i in range(2, 100):
        if is_prime(i):
            primes.append(i)
    count = 0
    for p in primes:
        if a % p == 0:
            count += 1
    if count == 3:
        return True
    else:
        return False
