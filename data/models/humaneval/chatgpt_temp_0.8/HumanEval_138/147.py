def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0 or n < 8:
        # if n is odd or less than 8, it cannot be written as the sum of 4 positive even numbers
        return False
    else:
        # loop through all possible combinations of 4 even numbers that sum to n
        for i in range(2, n // 2 + 1, 2):
            for j in range(i, n // 2 + 1, 2):
                for k in range(j, n // 2 + 1, 2):
                    for l in range(k, n // 2 + 1, 2):
                        if i + j + k + l == n:
                            # if we find a combination that works, return True
                            return True
        # if we've gone through all possible combinations and haven't found one that works, return False
        return False
