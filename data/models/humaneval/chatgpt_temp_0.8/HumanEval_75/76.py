def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    primes = []
    for i in range(2, a):
        if is_prime(i):
            primes.append(i)
            if len(primes) == 3:
                break
    if len(primes) != 3:
        return False
    product = primes[0] * primes[1] * primes[2]
    return product == a
