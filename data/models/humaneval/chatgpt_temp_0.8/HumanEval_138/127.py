def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8:  # if the number is less than 8, it's not possible to write it as the sum of exactly 4 positive even numbers
        return False
    elif n % 4 == 0:  # if the number is divisible by 4, it can be written as the sum of 4 equal even numbers
        return True
    elif (n - 4) % 4 == 0:  # if the number minus 4 is divisible by 4, it can be written as the sum of 3 equal even numbers and 1 even number that's 4 less than the others
        return True
    else:
        return False  # otherwise, it can't be written as the sum of exactly 4 positive even numbers
