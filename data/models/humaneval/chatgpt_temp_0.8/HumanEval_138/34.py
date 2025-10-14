def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    # Check if the input is even and greater than or equal to 8
    if n % 2 == 1 or n < 8:
        return False
    
    # Iterate over all possible even numbers between 2 and n/2
    for i in range(2, n//2+1, 2):
        
        # Subtract the current even number from n and check if the result can be written as the sum of 3 even numbers
        remainder = n - i
        for j in range(2, remainder//2+1, 2):
            for k in range(2, remainder//2+1, 2):
                if j + k + remainder == n:
                    return True
                
    # If no combination of 4 even numbers adds up to n, return False
    return False
