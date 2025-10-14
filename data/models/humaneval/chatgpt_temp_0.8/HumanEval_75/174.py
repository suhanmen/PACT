def is_prime(num):
    """Helper function to check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def is_multiply_prime(a):
    """Function to check if a number is the multiplication of 3 prime numbers"""
    count = 0
    for i in range(2, a):
        if a % i == 0 and is_prime(i):
            count += 1
    return count == 3
