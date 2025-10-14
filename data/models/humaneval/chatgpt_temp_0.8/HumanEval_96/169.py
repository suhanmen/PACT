def count_up_to(n):
    primes = []
    if n > 1:
        for i in range(2, n):
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                primes.append(i)
    return primes
