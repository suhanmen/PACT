def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 4 != 0:  # if n is not a multiple of 4, return False
        return False
    for i in range(1, n//2+1):  # check all possible combinations of 4 even numbers
        for j in range(1, n//2+1):
            for k in range(1, n//2+1):
                for l in range(1, n//2+1):
                    if i*2 + j*2 + k*2 + l*2 == n:
                        return True
    return False  # if no combination adds up to n, return False
