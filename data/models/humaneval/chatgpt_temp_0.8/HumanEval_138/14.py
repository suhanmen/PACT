def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 4 != 0:          # n must be divisible by 4 to be written as the sum of exactly 4 even numbers
        return False
    even_num = n//4         # divide n by 4 to get the even number to be used for each summand
    return even_num % 2 == 0 # check that even_num itself is even
