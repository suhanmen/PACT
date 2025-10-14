def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # We can only create a sum of even numbers using even numbers
    # If n is odd, it cannot be written as a sum of even numbers
    if n % 2 == 1:
        return False
    
    # We need exactly 4 even numbers
    count = 0
    for i in range(1, n):
        if i % 2 == 0:
            count += 1
            if count == 4 and i == n:
                return True
            elif count == 4:
                return False
    return False
