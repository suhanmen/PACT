python
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
    if n % 2 != 0 or n < 8:
        return False
    else:
        return True
