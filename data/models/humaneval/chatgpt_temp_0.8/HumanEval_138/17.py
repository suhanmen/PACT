def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0 or n < 8:
        # n is not even or not large enough to be written as the sum of 4 positive even numbers
        return False
    else:
        # Check all possible combinations of 4 positive even numbers that sum up to n
        for i in range(2, n//2 + 1, 2):
            for j in range(2, (n-i)//2 + 1, 2):
                for k in range(2, (n-i-j)//2 + 1, 2):
                    l = n-i-j-k
                    if l % 2 == 0:
                        # Found a combination of 4 positive even numbers that sum up to n
                        return True
        # Could not find any combination of 4 positive even numbers that sum up to n
        return False
