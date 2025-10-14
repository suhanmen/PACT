def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0 or n < 8:
        return False
    else:
        for i in range(2, int(n/2)+1, 2):
            for j in range(2, int(n/2)+1, 2):
                if i+j < n and (n-i-j) % 2 == 0:
                    return True
        return False
