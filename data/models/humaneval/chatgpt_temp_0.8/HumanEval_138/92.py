def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8: # If n is less than 8, it is impossible to write it as the sum of exactly 4 positive even numbers
        return False
    else:
        for i in range(2, n // 2 + 1, 2): # Check all even numbers between 2 and n/2 (inclusive)
            if (n - i) % 2 == 0: # Check if the remaining number can be written as the sum of 3 even numbers
                return True
        return False # Otherwise, it is impossible to write n as the sum of exactly 4 positive even numbers
