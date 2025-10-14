def double_the_difference(lst):
    sum_of_squared_odds = 0
    for num in lst:
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            sum_of_squared_odds += num**2
    return sum_of_squared_odds * 2
