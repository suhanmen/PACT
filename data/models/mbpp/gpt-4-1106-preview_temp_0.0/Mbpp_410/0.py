"""
Write a function to find the minimum value in a given heterogeneous list.
assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
"""



def min_val(hetero_list):
    # Filter out non-numeric values from the list
    numeric_values = [x for x in hetero_list if isinstance(x, (int, float))]
    # Return the minimum value from the filtered numeric values
    return min(numeric_values)

# Example usage
# assert min_val(['Python', 3, 2, 4, 5, 'version']) == 2
