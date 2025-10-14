def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    for a in range(2, n-6, 2):
        for b in range(a+2, n-4, 2):
            for c in range(b+2, n-2, 2):
                d = n - a - b - c
                if d > c and d % 2 == 0:
                    return True
    return False
