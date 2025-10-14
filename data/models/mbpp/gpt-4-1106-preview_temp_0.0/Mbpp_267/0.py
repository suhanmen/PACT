"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""



def square_sum(n):
    sum_of_squares = 0
    odd_number = 1
    for _ in range(n):
        sum_of_squares += odd_number ** 2
        odd_number += 2
    return sum_of_squares

assert square_sum(2) == 10
