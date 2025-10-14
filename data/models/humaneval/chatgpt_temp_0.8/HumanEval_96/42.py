def count_up_to(n):
    if n < 2:
        return []
    
    primes = [2]  # start with 2 as the first prime number
    num = 3      # start checking for primes from 3
    
    while len(primes) < n and num < n:
        is_prime = True
        
        # check if num is divisible by any prime number in primes list
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(num)
        
        num += 2  # move to next odd number
    
    return primes[:n]
