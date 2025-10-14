def count_up_to(n):
    if n <= 1:  # if n is 0 or 1, return empty list
        return []
    
    primes = [2]  # start with 2, the first prime number
    
    for num in range(3, n):
        is_prime = True
        for divisor in range(2, int(num**0.5)+1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    
    return primes
