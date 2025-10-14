def count_up_to(n):
    if n <= 1:
        return []
    primes = [2]  # start with 2, the first prime number
    p = 3  # start checking numbers from 3
    while len(primes) < n:
        is_prime = True
        # check if p is divisible by any previous prime numbers
        for prime in primes:
            if p % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(p)
        p += 2  # only check odd numbers
        if p > n:
            break
    return primes[:n]
