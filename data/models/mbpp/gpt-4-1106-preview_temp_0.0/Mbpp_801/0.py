"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""



def test_three_equal(a, b, c):
    # Count the number of equal numbers
    numbers = [a, b, c]
    unique_numbers = set(numbers)
    if len(unique_numbers) == 1:
        return 3
    elif len(unique_numbers) == 2:
        return 2
    else:
        return 0

# Example usage:
# result = test_three_equal(1, 1, 1)
# print('Number of equal integers:', result)
