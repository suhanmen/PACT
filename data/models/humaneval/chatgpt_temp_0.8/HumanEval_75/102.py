def is_multiply_prime(a):
    # initialize a counter for the number of prime factors
    count = 0
    
    # check if a is divisible by 2
    while a % 2 == 0:
        count += 1
        a //= 2
    
    # check if a is divisible by odd numbers up to its square root
    i = 3
    while i*i <= a and count < 3:
        while a % i == 0:
            count += 1
            a //= i
        i += 2
    
    # if a is still greater than 1, it must be prime
    if a > 1:
        count += 1
    
    return count == 3
