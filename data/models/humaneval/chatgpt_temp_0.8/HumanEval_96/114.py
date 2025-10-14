def count_up_to(n):
    if n < 2:
        return []
    primes = [2]
    num = 3
    while num < n:
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 2
    return primes
