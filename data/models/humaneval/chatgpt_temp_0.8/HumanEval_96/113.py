def count_up_to(n):
    if n <= 1:
        return []
    
    primes = [2]
    num = 3
    
    while len(primes) < n and num < n:
        is_prime = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(num)
        
        num += 2
    
    return primes[:n]
