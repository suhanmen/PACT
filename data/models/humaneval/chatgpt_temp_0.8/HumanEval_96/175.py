def count_up_to(n):
    primes = []
    for i in range(2, n):
        if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
            primes.append(i)
            if len(primes) == n:
                break
    return primes
