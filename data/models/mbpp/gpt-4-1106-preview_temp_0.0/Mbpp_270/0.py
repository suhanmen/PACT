"""
Write a python function to find the sum of even numbers at even positions of a list.
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
"""



def sum_even_and_even_index(numbers):
    return sum(num for idx, num in enumerate(numbers) if idx % 2 == 0 and num % 2 == 0)


assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
