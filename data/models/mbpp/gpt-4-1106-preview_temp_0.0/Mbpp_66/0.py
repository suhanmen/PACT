"""
Write a python function to count the number of positive numbers in a list.
assert pos_count([1,-2,3,-4]) == 2
"""



def pos_count(numbers):
    # Count the number of positive numbers in the list
    count = sum(1 for num in numbers if num > 0)
    return count

# Example usage
# assert pos_count([1, -2, 3, -4]) == 2
