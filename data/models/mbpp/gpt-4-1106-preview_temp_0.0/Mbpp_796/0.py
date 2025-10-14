"""
Write function to find the sum of all items in the given dictionary.
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
"""



def return_sum(numbers_dict):
    return sum(numbers_dict.values())

# Example usage
# assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
