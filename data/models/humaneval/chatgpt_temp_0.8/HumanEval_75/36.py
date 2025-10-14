def is_multiply_prime(a):
    # Check if a is less than 2 which is not a prime number.
    # If true, return False.
    if a < 2:
        return False
    
    # Create a list of prime numbers from 2 to a.
    primes = []
    for i in range(2, a+1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    
    # Check if there are at least 3 prime numbers in the list.
    if len(primes) < 3:
        return False
    
    # Check if the multiplication of any 3 prime numbers in the list is equal to a.
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            for k in range(j+1, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    
    return False
