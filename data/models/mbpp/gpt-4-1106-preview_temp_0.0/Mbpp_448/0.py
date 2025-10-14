"""
Write a function to calculate the sum of perrin numbers.
assert cal_sum(9) == 49
"""



def perrin_number(n):
    if n == 0:
        return 3
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return perrin_number(n - 2) + perrin_number(n - 3)


def cal_sum(n):
    sum_perrin = 0
    for i in range(n):
        sum_perrin += perrin_number(i)
    return sum_perrin

# Example usage
# print(cal_sum(9))  # Should output 49

assert cal_sum(9) == 49
