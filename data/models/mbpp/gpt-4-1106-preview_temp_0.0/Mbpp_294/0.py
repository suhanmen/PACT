"""
Write a function to find the maximum value in a given heterogeneous list.
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
"""



def max_val(heterogeneous_list):
    # Filter out non-numeric values from the list
    numeric_values = [x for x in heterogeneous_list if isinstance(x, (int, float))]
    # Return the maximum numeric value
    return max(numeric_values)

# Example usage
# assert max_val(['Python', 3, 2, 4, 5, 'version']) == 5
