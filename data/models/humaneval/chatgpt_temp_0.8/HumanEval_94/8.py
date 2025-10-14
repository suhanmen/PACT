def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.
    """
    
    # A helper function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    # Initialize variables for largest prime found and its sum of digits
    largest_prime = None
    largest_prime_digit_sum = 0
    
    # Loop through the list and look for the largest prime
    for num in lst:
        if is_prime(num):
            if largest_prime is None or num > largest_prime:
                largest_prime = num
    
    # If a prime was found, calculate the sum of its digits
    if largest_prime is not None:
        for digit in str(largest_prime):
            largest_prime_digit_sum += int(digit)
            
    return largest_prime_digit_sum
