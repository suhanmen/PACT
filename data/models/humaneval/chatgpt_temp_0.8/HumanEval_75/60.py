def is_multiply_prime(a):
    primes = []
    for num in range(2, 100):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
    
    count = 0
    for p in primes:
        if a % p == 0:
            count += 1
        if count == 3 and a != p*p*p:
            return True
    return False
