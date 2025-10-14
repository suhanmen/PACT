def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    # Check if the number is less than or equal to 1
    if a <= 1:
        return False

    # Check if the number is even
    if a % 2 == 0:
        # Check if the number is divisible by 2, 3, and another prime number
        for i in range(3, a):
            if a % i == 0 and is_prime(i) and is_prime(a // i):
                return True
        return False
    else:
        # Check if the number is divisible by 3, 5, and another prime number
        for i in range(5, a):
            if a % i == 0 and is_prime(i) and is_prime(a // i) and is_prime(3):
                return True
        return False
