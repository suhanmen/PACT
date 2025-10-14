def is_multiply_prime(a):
    # First, find all prime numbers less than a
    primes = [2] # 2 is the smallest prime
    for i in range(3, a):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    # Check if a is the product of 3 primes
    count = 0
    for p in primes:
        if a % p == 0:
            count += 1
            if count == 3:
                return True
    return False
