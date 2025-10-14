def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0 or n < 8:
        return False
    
    for i in range(1, n//2 + 1):
        for j in range(i, n//2 + 1):
            for k in range(j, n//2 + 1):
                l = n - i - j - k
                if l >= k and l % 2 == 0:
                    return True
    
    return False
