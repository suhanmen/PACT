def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in primes:
        if a % i == 0:
            for j in primes:
                if a % (i*j) == 0 and i*j != a:
                    for k in primes:
                        if a == i*j*k:
                            return True
    return False
