"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""



def count_first_elements(input_tuple):
    for index, element in enumerate(input_tuple):
        if isinstance(element, tuple):
            return index
    return None  # In case there is no tuple in the input

# Example usage
# assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3
