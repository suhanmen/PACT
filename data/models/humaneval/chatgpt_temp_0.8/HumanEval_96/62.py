def count_up_to(n):
    if n < 2:
        return []
    primes = [2]
    i = 3
    while len(primes) < n and i < n:
        if all(i % p != 0 for p in primes):
            primes.append(i)
        i += 2
    return primes[:n]
