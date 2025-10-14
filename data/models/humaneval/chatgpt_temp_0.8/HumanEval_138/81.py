def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
    if n % 2 != 0:
        # if n is not an even number, it cannot be written as the sum of even numbers
        return False
    for i in range(1, n//2 + 1):
        for j in range(1, n//2 + 1):
            for k in range(1, n//2 + 1):
                for l in range(1, n//2 + 1):
                    if 2*i + 2*j + 2*k + 2*l == n:
                        return True
    return False
