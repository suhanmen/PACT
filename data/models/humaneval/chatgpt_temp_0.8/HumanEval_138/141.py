def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
    count = 0
    for i in range(2, n):
        if i % 2 == 0 and n - i > 0:
            count += 1
            if count == 4:
                return True
    return False
