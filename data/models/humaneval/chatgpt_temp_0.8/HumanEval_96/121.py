def count_up_to(n):
    if n <= 1:
        return []
    
    # create a boolean array "is_prime[0..n]" and initialize all entries it as true
    is_prime = [True for i in range(n)]
    p = 2
    while p * p <= n:
        # If is_prime[p] is not changed, then it is a prime
        if is_prime[p]:
            # Update all multiples of p
            for i in range(p * 2, n, p):
                is_prime[i] = False
        p += 1
    
    # return all prime numbers less than n
    primes = [i for i in range(2, n) if is_prime[i]]
    return primes[:n]
