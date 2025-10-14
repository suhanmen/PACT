"""
Write a function to sort each sublist of strings in a given list of lists.
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""



def sort_sublists(list_of_lists):
    return [sorted(sublist) for sublist in list_of_lists]

# Example usage
# sorted_lists = sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])
# print(sorted_lists)  # Output: [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
