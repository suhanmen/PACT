def is_multiply_prime(a):
    """Returns True if a is the multiplication of 3 prime numbers, False otherwise."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    count = 0
    for p in primes:
        if a % p == 0:
            count += 1
            a //= p
            if count == 3:
                break
    return count == 3 and a == 1
