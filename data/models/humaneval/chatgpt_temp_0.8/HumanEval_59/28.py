def largest_prime_factor(n: int):
    # Initialize the largest prime factor to 1
    largest = 1
    
    # Check for factors up to the square root of n
    for i in range(2, int(n**0.5)+1):
        # If i is a factor of n, test if it is prime
        if n % i == 0:
            is_prime = True
            # Check if i is prime
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    is_prime = False
                    break
            # If i is prime and larger than the current largest, update the largest
            if is_prime and i > largest:
                largest = i
    
    # Return the largest prime factor
    return largest
