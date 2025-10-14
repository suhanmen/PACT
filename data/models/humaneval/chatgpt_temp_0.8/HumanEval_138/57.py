def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8:
        return False
    even_count = 0
    while n > 0 and even_count < 4:
        if n % 2 == 0:
            n -= 2
            even_count += 1
        else:
            n -= 1
    return even_count == 4 and n == 0
