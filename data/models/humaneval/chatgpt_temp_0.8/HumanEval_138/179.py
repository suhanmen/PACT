def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    count = 0
    for i in range(2, n, 2):
        if n - i >= 2 and count < 3:
            count += 1
            n -= i
    return count == 3 and n % 2 == 0
