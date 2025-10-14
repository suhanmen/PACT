def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0:
        # if n is odd, it cannot be written as sum of even numbers
        return False
    elif n == 8:
        # special case, as 8 can be written as sum of 4 even numbers in only one way
        return True
    else:
        # check if n - 2 * x can be written as sum of 3 even numbers
        for x in range(1, n // 2):
            if (n - 2 * x) % 4 == 0:
                return True
        return False
