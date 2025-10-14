def count_up_to(n):
    if n < 2:
        return []

    primes = []
    for num in range(2, n):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            if len(primes) == n:
                break

    return primes
