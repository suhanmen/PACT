def count_up_to(n):
    if n < 2:
        return []
    primes = [2]
    num = 3
    while len(primes) < n and num < n:
        for prime in primes:
            if num % prime == 0:
                break
        else:
            primes.append(num)
        num += 2
    return primes[:n]
