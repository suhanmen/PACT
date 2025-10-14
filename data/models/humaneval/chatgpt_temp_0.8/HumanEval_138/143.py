def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    even_count = 0
    for i in range(1, n):
        if i % 2 == 0 and n - i >= 2 and even_count < 3:
            even_count += 1
            n -= i
    return even_count == 3 and n % 2 == 0
