def double_the_difference(lst):
    total = 0
    for num in lst:
        if type(num) == int and num >= 0 and num % 2 == 1:
            total += num**2
    return total * 2
