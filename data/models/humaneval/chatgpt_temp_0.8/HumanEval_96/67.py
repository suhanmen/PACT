def count_up_to(n):
    if n <= 1:
        return []

    primes = [2]
    i = 3

    while i < n:
        is_prime = True

        for j in primes:
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)

        i += 2

    return primes
