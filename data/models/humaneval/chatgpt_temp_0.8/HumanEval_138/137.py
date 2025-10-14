def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0:  # n is odd
        return False
    
    max_numbers = min(n//2, 4)  # maximum number of even numbers that can add up to n
    for i in range(1, max_numbers+1):
        remaining_sum = n - 2*i
        if remaining_sum % 2 == 0 and remaining_sum <= 2*(4-i):
            return True
    return False
