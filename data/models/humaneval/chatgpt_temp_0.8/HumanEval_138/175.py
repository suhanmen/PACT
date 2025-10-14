def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8: # If n is less than 8, it can't be written as the sum of 4 positive even numbers
        return False
    elif n % 2 != 0: # If n is odd, it can't be written as the sum of even numbers
        return False
    else:
        # Loop through all possible values of the first even number (up to half of n)
        for i in range(2, n//2 + 1, 2):
            # Calculate the remaining sum by subtracting the current even number from n
            remaining_sum = n - i
            # Loop through all possible values of the second even number (up to half of the remaining sum)
            for j in range(2, remaining_sum//2 + 1, 2):
                # Calculate the remaining sum again
                remaining_sum2 = remaining_sum - j
                # Loop through all possible values of the third even number (up to half of the remaining sum)
                for k in range(2, remaining_sum2//2 + 1, 2):
                    # Calculate the fourth even number by subtracting the current ev
