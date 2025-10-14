def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    count = 0
    for i in range(2, n//2 + 1, 2):
        for j in range(i, n//2 + 1, 2):
            for k in range(j, n//2 + 1, 2):
                if i + j + k <= n:
                    if (n - i - j - k) % 2 == 0 and (n - i - j - k) >= 2:
                        count += 1
    return count == 1
