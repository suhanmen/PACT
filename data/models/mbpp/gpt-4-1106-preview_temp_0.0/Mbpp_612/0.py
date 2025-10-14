"""
Write a python function which takes a list of lists, where each sublist has two elements, and returns a list of two lists where the first list has the first element of each sublist and the second one has the second.
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
"""



def merge(list_of_lists):
    first_elements = [sublist[0] for sublist in list_of_lists]
    second_elements = [sublist[1] for sublist in list_of_lists]
    return [first_elements, second_elements]

# Example usage
# merged_list = merge([['x', 'y'], ['a', 'b'], ['m', 'n']])
# print(merged_list)  # Output: [['x', 'a', 'm'], ['y', 'b', 'n']]
