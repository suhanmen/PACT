def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
    if n < 8:
        return False
    else:
        for i in range(2, n-3, 2):
            for j in range(i, n-1, 2):
                for k in range(j, n, 2):
                    for l in range(k, n+1, 2):
                        if i + j + k + l == n:
                            return True
        return False
