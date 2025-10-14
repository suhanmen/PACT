"""
Write a python function that takes in an integer n and finds the sum of the first n even natural numbers that are raised to the fifth power.
assert even_Power_Sum(2) == 1056
"""



def even_Power_Sum(n):
    sum_of_powers = 0
    for i in range(1, n+1):
        even_number = 2 * i
        sum_of_powers += even_number ** 5
    return sum_of_powers

# Example usage:
# result = even_Power_Sum(2)
# print(result)  # Output should be 1056
