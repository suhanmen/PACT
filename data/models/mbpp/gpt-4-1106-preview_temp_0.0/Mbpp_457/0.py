"""
Write a python function to find the sublist having minimum length.
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
"""



def Find_Min(list_of_sublists):
    if not list_of_sublists:
        return []
    min_length = float('inf')
    min_sublist = []
    for sublist in list_of_sublists:
        if len(sublist) < min_length:
            min_length = len(sublist)
            min_sublist = sublist
    return min_sublist

assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
