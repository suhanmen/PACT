def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_numbers = []
    for num in range(2, 100):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_numbers.append(num)

    count = 0
    for prime in prime_numbers:
        if a % prime == 0:
            count += 1
    if count == 3:
        return True
    else:
        return False
