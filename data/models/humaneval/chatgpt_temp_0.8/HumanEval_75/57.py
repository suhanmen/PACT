def is_multiply_prime(a):
    primes = []
    for num in range(2, a):
        if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
            primes.append(num)
    
    count = 0
    for prime in primes:
        if a % prime == 0:
            count += 1
    if count == 3:
        return True
    else:
        return False
