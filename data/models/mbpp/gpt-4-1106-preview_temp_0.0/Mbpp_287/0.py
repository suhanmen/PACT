"""
Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
assert square_Sum(2) == 20
"""



def square_sum(n):
    sum_of_squares = 0
    for i in range(1, n+1):
        sum_of_squares += (2*i)**2
    return sum_of_squares

# Example usage:
# result = square_sum(2)
# print(result)  # Output will be 20

assert square_sum(2) == 20
