def is_multiply_prime(a):
    # Check if the given number is less than 2 or greater than 97, which are not prime numbers
    if a < 2 or a > 97:
        return False
    
    # Find the prime factors of the given number
    factors = []
    for i in range(2, a+1):
        while a % i == 0:
            factors.append(i)
            a //= i
        if a == 1:
            break
    
    # Check if the number has exactly 3 prime factors
    if len(factors) != 3:
        return False
    
    # Check if all 3 factors are prime
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for factor in factors:
        if factor not in primes:
            return False
    
    return True
