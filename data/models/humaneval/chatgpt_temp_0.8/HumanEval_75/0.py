def is_multiply_prime(a):
    primes = [] # initialize an empty list to store prime numbers
    for num in range(2, 100):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num) # add the prime number to the list
    # check if the given number is the multiplication of 3 prime numbers
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            for k in range(j+1, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False
