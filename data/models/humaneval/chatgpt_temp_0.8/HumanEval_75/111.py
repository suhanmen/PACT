def is_multiply_prime(a):
    primes = []
    for num in range(2, a+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    count = 0
    for prime in primes:
        if a % prime == 0:
            count += 1
    if count == 3:
        return True
    else:
        return False
