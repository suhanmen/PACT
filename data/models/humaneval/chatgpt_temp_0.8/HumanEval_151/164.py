def double_the_difference(lst):
    sum_of_squares = 0
    for num in lst:
        if type(num) == int and num >= 0 and num % 2 == 1:
            sum_of_squares += num**2
    return 2*sum_of_squares
