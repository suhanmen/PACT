def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8:  # If n is less than 8, it can't be written as the sum of 4 positive even numbers
        return False
    elif n % 4 != 0:  # If n is not divisible by 4, it can't be written as the sum of 4 positive even numbers
        return False
    else:
        return True
