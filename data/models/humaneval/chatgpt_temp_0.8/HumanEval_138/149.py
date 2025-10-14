def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0:  # if n is odd, it cannot be written as the sum of even numbers
        return False

    count = 0  # count the number of even numbers
    for i in range(2, n // 2 + 1, 2):
        if (n - i) % 2 == 0:  # if the difference is even, we have found another even number that can be added to the sum
            count += 1
            if count == 3:  # if we have found 3 even numbers, the fourth one can be calculated by subtracting the sum of the other 3 from n
                return True

    return False  # if we have not found 4 even numbers, return False
