def next_smallest(lst):
    if len(lst) < 2:  # If there are less than 2 elements in the list, return None
        return None
    lst = list(set(lst))  # Convert to a set to remove duplicates, then back to a list
    lst = sorted(lst)  # Sort the list
    if len(lst) < 2:  # If there are less than 2 unique elements in the list, return None
        return None
    return lst[1]  # Return the second smallest element
