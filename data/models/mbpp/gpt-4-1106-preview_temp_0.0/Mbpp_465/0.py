"""
Write a function to drop empty items from a given dictionary.
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
"""

def drop_empty(input_dict):
    return {k: v for k, v in input_dict.items() if v is not None}

# Example usage:
# cleaned_dict = drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': None})
# print(cleaned_dict)  # Output: {'c1': 'Red', 'c2': 'Green'}