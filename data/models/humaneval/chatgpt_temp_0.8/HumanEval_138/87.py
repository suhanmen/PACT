def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0:
        return False
    for i in range(1, n//2):
        for j in range(1, n//2):
            for k in range(1, n//2):
                for l in range(1, n//2):
                    if i % 2 == 0 and j % 2 == 0 and k % 2 == 0 and l % 2 == 0 and i + j + k + l == n:
                        return True
    return False
