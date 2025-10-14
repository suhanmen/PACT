def count_up_to(n):
    if n <= 1:
        return []
    
    # Initialize a boolean array to mark all numbers as prime initially
    primes = [True] * n
    
    # Mark numbers that are not prime
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = False
    
    # Collect all prime numbers into a list
    result = []
    for i in range(2, n):
        if primes[i]:
            result.append(i)
            if len(result) == n:
                break
                
    return result
