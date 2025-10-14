def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check if the number is even and greater than or equal to 8
    if n % 2 == 0 and n >= 8:
        # Check all possible combinations of four positive even numbers that add up to n
        for i in range(2, n // 2 + 1, 2):
            for j in range(2, n // 2 + 1, 2):
                for k in range(2, n // 2 + 1, 2):
                    for l in range(2, n // 2 + 1, 2):
                        if i + j + k + l == n:
                            return True
    return False
