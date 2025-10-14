"""
Write a function to flatten the list of lists into a single set of numbers.
assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
"""



def extract_singly(list_of_tuples):
    return {num for tup in list_of_tuples for num in tup}

# Example usage:
# flattened_set = extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])
# print(flattened_set)  # Output: {1, 3, 4, 5, 7}
