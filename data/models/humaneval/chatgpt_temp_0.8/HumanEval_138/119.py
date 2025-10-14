def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8:  # If the number is less than 8, it cannot be written as the sum of exactly 4 positive even numbers
        return False

    for i in range(2, n - 3, 2):  # Starting from 2, check all possible even numbers as the first number
        for j in range(i, n - 1, 2):  # Starting from i, check all possible even numbers as the second number
            for k in range(j, n, 2):  # Starting from j, check all possible even numbers as the third number
                if i + j + k == n:  # If the sum of the first three numbers is equal to n, check if the fourth number is even
                    if (n - i - j - k) % 2 == 0:  # If the fourth number is even, return True
                        return True

    return False  # If no combination of even numbers adds up to n, return False
