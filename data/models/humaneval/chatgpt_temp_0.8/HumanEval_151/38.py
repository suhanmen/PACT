def double_the_difference(lst):
    odd_numbers = [x for x in lst if x > 0 and type(x) == int and x % 2 != 0]
    sum_of_squares = sum([x**2 for x in odd_numbers])
    return sum_of_squares * 2
