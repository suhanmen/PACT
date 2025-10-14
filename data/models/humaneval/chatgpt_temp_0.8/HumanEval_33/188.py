def sort_third(l: list):
    # create a copy of the original list
    l_sorted = l.copy()
    # sort every third element of the sorted list
    for i in range(2, len(l), 3):
        l_sorted[i] = sorted(l[i-2:i+1])[1]  # middle element after sorting
    return l_sorted
