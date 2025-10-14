def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    # If n is less than 8 or odd, we cannot find 4 positive even numbers that add up to n
    if n < 8 or n % 2 == 1:
        return False

    # We can start with 2, 4, 6, and 8 and keep adding 2 to each number until we reach n
    # If we ever exceed n, then it's not possible to add up to n with 4 positive even numbers
    for i in range(2, n, 2):
        for j in range(i, n, 2):
            for k in range(j, n, 2):
                for l in range(k, n, 2):
                    if i + j + k + l == n:
                        return True
                    elif i + j + k + l > n:
                        break

    return False
