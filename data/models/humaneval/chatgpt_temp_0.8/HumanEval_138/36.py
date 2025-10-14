def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8:
        return False
    # We can try all possible values for the first two even numbers
    for i in range(2, n - 4, 2):
        for j in range(i, n - 2, 2):
            # Check if the remaining sum can be written as 2 even numbers
            if (n - i - j) % 2 == 0:
                return True
    return False
