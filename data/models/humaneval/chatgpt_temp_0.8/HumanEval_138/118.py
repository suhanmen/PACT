def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 4 != 0:  # If n is not divisible by 4, it can't be written as the sum of 4 even numbers
        return False

    # Check if the sum of 4 even numbers can be equal to n
    for i in range(1, n // 2 + 1):
        if i % 2 == 0 and (n - i) % 2 == 0:
            return True

    return False
