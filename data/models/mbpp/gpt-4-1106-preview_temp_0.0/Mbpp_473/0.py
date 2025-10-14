"""
Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
"""



def tuple_intersection(list1, list2):
    # Convert tuples in list2 to sets for easy comparison
    set_list2 = {frozenset(tup) for tup in list2}
    # Find intersection by checking if tuple from list1 as set is in set_list2
    intersection = {tuple(tup) for tup in list1 if frozenset(tup) in set_list2}
    return intersection

# Example usage
# assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
