def count_up_to(n):
    primes = []
    if n > 1:
        primes.append(2)
    for i in range(3, n):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes
