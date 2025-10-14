def count_up_to(n):
    if n < 2:
        return []
    primes = [2]
    next_num = 3
    while next_num < n:
        is_prime = True
        for prime in primes:
            if prime * prime > next_num:
                break
            if next_num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(next_num)
        next_num += 2
    return primes
