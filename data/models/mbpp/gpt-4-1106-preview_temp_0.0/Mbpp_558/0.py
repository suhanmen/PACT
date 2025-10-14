"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(1,2) == 1
"""



def digit_distance_nums(num1, num2):
    str_num1, str_num2 = str(num1), str(num2)
    if len(str_num1) != len(str_num2):
        raise ValueError('Numbers must have the same number of digits')

    return sum(abs(int(d1) - int(d2)) for d1, d2 in zip(str_num1, str_num2))

# Example usage:
# result = digit_distance_nums(123, 321)
# print(result)  # Output: 4 (|1-3| + |2-2| + |3-1|)

# Test case:
assert digit_distance_nums(1, 2) == 1
