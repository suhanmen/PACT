def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # We can only represent n as a sum of even numbers if n is even
    if n % 2 != 0:
        return False
    
    # Check all possible combinations of 4 positive even numbers
    for a in range(2, n, 2):
        for b in range(2, n-a, 2):
            for c in range(2, n-a-b, 2):
                d = n - a - b - c
                if d % 2 == 0 and d >= 2:
                    return True
    
    # If no combination of 4 positive even numbers adds up to n, return False
    return False
