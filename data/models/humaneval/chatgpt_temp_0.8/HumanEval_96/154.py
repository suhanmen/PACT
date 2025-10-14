def count_up_to(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes
