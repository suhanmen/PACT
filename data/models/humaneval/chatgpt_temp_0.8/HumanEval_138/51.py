def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8:  # n cannot be written as the sum of 4 even numbers if it is less than 8
        return False
    
    # We know that the four even numbers will sum to n, so each even number must be less than or equal to n/4
    max_even = n // 4  # integer division to get the largest even number
    
    # We can use a nested loop to try every combination of four even numbers
    for i in range(2, max_even+1, 2):  # start at 2 and step by 2 to only consider even numbers
        for j in range(2, max_even+1, 2):
            for k in range(2, max_even+1, 2):
                for l in range(2, max_even+1, 2):
                    if i + j + k + l == n:  # check if this combination sums to n
                        return True
    
    # If we get here, we have exhausted all possible combinations without finding a valid one
    return False
