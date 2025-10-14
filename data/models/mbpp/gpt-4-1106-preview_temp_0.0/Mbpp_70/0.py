"""
Write a function to find whether all the given tuples have equal length or not.
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
"""



def get_equal(tuples_list):
    if not tuples_list:  # Check if the list is empty
        return True
    first_length = len(tuples_list[0])
    return all(len(t) == first_length for t in tuples_list)

# Example usage
# assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
