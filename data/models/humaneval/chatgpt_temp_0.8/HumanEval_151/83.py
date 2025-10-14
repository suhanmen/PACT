def double_the_difference(lst):
    odd_numbers = [num for num in lst if num > 0 and num % 2 != 0 and isinstance(num, int)]
    sum_of_squares = sum([num ** 2 for num in odd_numbers])
    return sum_of_squares * 2
