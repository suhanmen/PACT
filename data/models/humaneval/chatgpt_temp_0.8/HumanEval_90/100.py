def next_smallest(lst):
    if len(lst) < 2:  # Check if the list has at least two elements
        return None
    else:
        # Remove duplicates and sort in ascending order
        lst = sorted(set(lst))
        if len(lst) < 2:  # Check if the list has at least two unique elements
            return None
        else:
            return lst[1]  # Return the second smallest element
