def count_up_to(n):
    # Define a function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
    # Create an empty list to store the prime numbers
    primes = []
    
    # Iterate over numbers from 2 to n-1
    for i in range(2, n):
        # If i is prime, add it to the list
        if is_prime(i):
            primes.append(i)
    
    # Return the list of prime numbers
    return primes
