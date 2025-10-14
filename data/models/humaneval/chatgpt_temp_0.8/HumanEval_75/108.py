# Define a helper function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Define the main function
def is_multiply_prime(a):
    # List the prime numbers less than a
    primes = [n for n in range(2, a) if is_prime(n)]
    
    # Check all possible combinations of 3 prime numbers that multiply to a
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            for k in range(j+1, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
                
    return False
