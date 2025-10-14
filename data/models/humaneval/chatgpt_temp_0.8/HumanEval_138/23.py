def is_equal_to_sum_even(n):
    """
    Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    """
    if n % 2 != 0:
        return False  # n must be even to be written as the sum of even numbers
    for i in range(2, (n // 2) + 1, 2):
        for j in range(i, (n // 2) + 1, 2):
            for k in range(j, (n // 2) + 1, 2):
                if i + j + k + k == n:
                    return True
    return False
