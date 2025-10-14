def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 4 != 0:  # if n is not divisible by 4, it cannot be written as the sum of 4 even numbers
        return False
    for i in range(1, n//2 + 1):  # check all possible combinations of even numbers that add up to n
        for j in range(i, n//2 + 1):
            for k in range(j, n//2 + 1):
                for l in range(k, n//2 + 1):
                    if i % 2 == 0 and j % 2 == 0 and k % 2 == 0 and l % 2 == 0 and i + j + k + l == n:
                        return True
    return False
