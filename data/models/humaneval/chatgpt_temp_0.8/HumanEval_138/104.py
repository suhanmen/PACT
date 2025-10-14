def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8:  # if n is less than 8, it cannot be represented as the sum of 4 positive even numbers.
        return False 
    
    # we need to find 4 positive even numbers such that their sum is equal to n.
    for i in range(2, n):
        if i % 2 == 0:  # if i is even
            for j in range(2, n):
                if j % 2 == 0:  # if j is even
                    for k in range(2, n):
                        if k % 2 == 0:  # if k is even
                            for l in range(2, n):
                                if l % 2 == 0: # if l is even
                                    if i + j + k + l == n: # if sum of these 4 even numbers is equal to n
                                        return True
    return False  # if no 4 positive even numbers are found such that their sum is equal to n.
