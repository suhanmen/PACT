"""
Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
"""



def sample_nam(names):
    # Filter out names that start with a lowercase letter
    filtered_names = [name for name in names if name[0].isupper()]
    # Sum the lengths of the remaining names
    return sum(len(name) for name in filtered_names)

# Example usage
# assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']) == 16
