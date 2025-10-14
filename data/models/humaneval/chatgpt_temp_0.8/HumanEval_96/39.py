def count_up_to(n):
    if n < 2:
        return []
    primes = [2]
    i = 3
    while len(primes) < n and i < n:
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
        i += 2
    return primes
