"""
Write a function to check if all the elements in tuple have same data type or not.
assert check_type((5, 6, 7, 3, 5, 6) ) == True
"""



def check_type(input_tuple):
    if not input_tuple:  # Check if the tuple is empty
        return True
    first_type = type(input_tuple[0])
    return all(type(element) == first_type for element in input_tuple)

# Example usage:
# assert check_type((5, 6, 7, 3, 5, 6)) == True
