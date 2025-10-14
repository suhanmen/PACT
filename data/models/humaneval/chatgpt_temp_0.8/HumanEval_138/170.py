def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    count = 0
    for i in range(2, n):
        if i % 2 == 0:
            for j in range(i, n):
                if j % 2 == 0:
                    for k in range(j, n):
                        if k % 2 == 0:
                            for l in range(k, n):
                                if l % 2 == 0:
                                    if i + j + k + l == n:
                                        return True
    return False
