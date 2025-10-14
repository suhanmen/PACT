def count_up_to(n):
    # If n is less than or equal to 1, return an empty list
    if n <= 1:
        return []
    
    # Create a list to store the prime numbers
    primes = []
    
    # Check each integer from 2 to n-1 for primality
    for i in range(2, n):
        is_prime = True
        # Check if i is divisible by any integer from 2 to i-1
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        # If i is prime, add it to the list of primes
        if is_prime:
            primes.append(i)
            # If we have already found n primes, return the list
            if len(primes) == n:
                return primes
    # If we have not found n primes, return the list of primes we have found
    return primes
