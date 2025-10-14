def double_the_difference(lst):
    sum_of_squares = 0
    for num in lst:
        if num > 0 and num % 2 == 1:
            sum_of_squares += num**2
    return sum_of_squares
