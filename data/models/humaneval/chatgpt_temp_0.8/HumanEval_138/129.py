def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8:
        return False
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] # list of even numbers
    for i in even_nums:
        for j in even_nums:
            for k in even_nums:
                for l in even_nums:
                    if i+j+k+l == n and len(set([i,j,k,l]))==4:
                        return True
    return False
