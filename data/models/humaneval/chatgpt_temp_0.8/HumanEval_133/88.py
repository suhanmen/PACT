def sum_squares(lst):
    result = 0
    for num in lst:
        result += (int(num+0.99)**2)
    return result
