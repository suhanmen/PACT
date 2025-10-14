"""
Write a function to find the sum of numbers in a list within a range specified by two indices.
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
"""



def sum_range_list(numbers, start_index, end_index):
    # Ensure the indices are within the list boundaries
    if start_index < 0 or end_index >= len(numbers):
        return 'Invalid index range'

    # Calculate the sum of the specified range
    return sum(numbers[start_index:end_index + 1])

# Example usage
# assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
