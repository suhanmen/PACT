def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8:  # If n is less than 8, it is impossible to express as the sum of 4 even numbers
        return False
    for i in range(2, n - 2, 2):
        # Iterate from 2 through n-2, checking all possible values for the first even number
        for j in range(i + 2, n - 2, 2):
            # Iterate from i+2 through n-2, checking all possible values for the second even number
            for k in range(j + 2, n - 2, 2):
                # Iterate from j+2 through n-2, checking all possible values for the third even number
                if i + j + k == n:  # If the sum of the first three even numbers equals n, check the fourth even number
                    if n - (i + j + k) % 2 == 0:  # If the fourth even number is also positive and even
                        return True
    return False  # If no combination of 4 even numbers sums to n, return False
