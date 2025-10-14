"""
Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
"""


def index_minimum(tuple_list):
    # Sort the list of tuples by the second element in each tuple
    sorted_list = sorted(tuple_list, key=lambda x: x[1])
    # Return the first element of the tuple with the smallest second value
    return sorted_list[0][0]

# Example usage
# assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
