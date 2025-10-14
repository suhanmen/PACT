def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check if n is less than 8 or odd
    if n < 8 or n % 2 != 0:
        return False
    # Check for all possible combinations of 4 even numbers that add up to n
    for i in range(2, n - 3, 2):
        for j in range(2, n - i - 1, 2):
            for k in range(2, n - i - j, 2):
                l = n - i - j - k
                # Check if all 4 numbers are even
                if l % 2 == 0 and l > 0:
                    return True
    return False
