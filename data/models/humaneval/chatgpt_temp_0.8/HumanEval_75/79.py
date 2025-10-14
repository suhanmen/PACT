def is_multiply_prime(a):
    # A list to store prime numbers
    primes = []
    # Loop to find all prime numbers less than a
    for num in range(2, a):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    # Loop to check if a is multiplication of 3 prime numbers
    count = 0
    for prime in primes:
        if a % prime == 0:
            count += 1
    if count == 3:
        return True
    else:
        return False
