def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8:  # if n is less than 8, it can't be written as the sum of 4 positive even numbers
        return False
    
    # iterate over all possible even numbers less than n and check if n - 2*even is divisible by 4
    for even in range(2, n, 2):
        if (n - 2*even) % 4 == 0:
            return True
    
    return False  # if no combination of 4 positive even numbers adds up to n, return False
