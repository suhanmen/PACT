"""
Write a python function to find the length of the smallest list in a list of lists.
assert Find_Min_Length([[1],[1,2]]) == 1
"""



def Find_Min_Length(list_of_lists):
    return min(len(lst) for lst in list_of_lists)

# Example usage:
# assert Find_Min_Length([[1],[1,2]]) == 1
