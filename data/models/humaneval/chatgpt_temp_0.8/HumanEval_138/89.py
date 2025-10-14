def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8: # Not enough even numbers to add up to n
        return False
    elif n == 8: # n is the sum of 4 even numbers: 2+2+2+2
        return True
    else:
        for i in range(2, n-6, 2): # Iterate through possible even numbers to add up to n
            for j in range(i, n-4, 2):
                for k in range(j, n-2, 2):
                    if i+j+k+n == 4*i: # Check if the sum is equal to 4 times one of the even numbers
                        return True
        return False
