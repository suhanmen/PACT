def sort_third(l: list):
    # Make a copy of the original list
    l_sorted = l.copy()
    # Sort every third element of the new list
    for i in range(2, len(l_sorted), 3):
        l_sorted[i] = sorted(l[i-2:i+1])[1]
    # Return the new list
    return l_sorted
