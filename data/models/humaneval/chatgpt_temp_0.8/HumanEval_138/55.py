def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8:
        return False
    else:
        for i in range(2, n):
            if i % 2 == 0:
                for j in range(2, n):
                    if j % 2 == 0:
                        for k in range(2, n):
                            if k % 2 == 0:
                                for l in range(2, n):
                                    if l % 2 == 0 and i+j+k+l == n:
                                        return True
        return False
