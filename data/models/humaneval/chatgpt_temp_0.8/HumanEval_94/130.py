def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.
    """
    def is_prime(n):
        """Helper function to check whether a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    largest_prime = 0
    for num in lst:
        if is_prime(num) and num > largest_prime:
            largest_prime = num
    
    if largest_prime == 0:
        return 0
    
    # Sum the digits of the largest prime number
    digit_sum = 0
    for digit in str(largest_prime):
        digit_sum += int(digit)
    
    return digit_sum
