python
def is_multiply_prime(a):
    # Check if the given number is less than 2, return False otherwise
    if a < 2:
        return False
    
    # Create a list of prime numbers less than 100
    prime_list = []
    for num in range(2, 100):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_list.append(num)
    
    # Check if the given number is the multiplication of 3 prime numbers
    factor_count = 0
    for prime in prime_list:
        if a % prime == 0:
            factor_count += 1
        if factor_count == 3:
            return True
    
    return False
